<script type="text/javascript">
        function googleTranslateElementInit() {
            new google.translate.TranslateElement({
                pageLanguage: 'auto',
                layout: google.translate.TranslateElement.InlineLayout.VERTICAL,
                autoDisplay: true
            }, 'google_translate_element');
        }
</script>
<script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Bungee Hairline&display=swap">

# Exploring Concurrency in Swift: Actors vs. Queues

Concurrency is a core concept for developing high-performance applications, and with Swift's recent advancements, understanding the new concurrency model is essential for modern iOS developers. The introduction of *actors* in Swift has generated discussions about their performance compared to traditional *queues*. To delve deeper into this, I have conducted a benchmark to compare the execution times of these two concurrency paradigms.

## What Are Actors?
In Swift, an *actor* is a type that protects access to its mutable state, ensuring that only one piece of code can access that state at a time, making it a thread-safe unit of work. This is particularly useful in concurrent environments where you need to avoid data races.

### The Significance of Actors in Swift Concurrency

In the realm of Swift concurrency, an *actor* is a pivotal type that serves to encapsulate mutable state and synchronize access to it. It employs a rigorous protocol to ensure that its state is only accessible via one thread at a time, effectively preventing simultaneous read and write operations, which can lead to unpredictable behavior or data corruption—commonly known as data races.

The actor model stands out by offering a structured concurrency mechanism that is easier to reason about compared to traditional lock-based concurrency. It provides a high level of abstraction that eliminates most opportunities for mistakes that can occur in complex multithreaded environments, such as deadlock, livelock, and race conditions. By enforcing serial access to its internal state, actors allow developers to write safe concurrent code without the intricate details of thread management and synchronization primitives.

Moreover, actors seamlessly integrate with Swift’s async/await syntax, further simplifying the asynchronous code by allowing it to read like synchronous, straightforward sequences of events. This integration enhances code clarity and maintainability, making it easier to predict the program flow and identify potential issues.

In essence, when dealing with concurrent programming in Swift, adopting actors can significantly reduce the complexity and risks associated with shared mutable state, making them an essential tool for developers striving for robust and efficient multithreading applications.

## Understanding the Limits of Actors in Preventing Data Races

Inspired by [Antoine van der Lee's insightful post](https://www.avanderlee.com/swift/actors/#why-data-races-can-still-occur-when-using-actors), it's important to recognize that while actors are a powerful tool for minimizing the risk of data races in concurrent Swift programming, they are not a panacea.

### Why Data Races Can Still Occur When Using Actors

Integrating actors into your Swift code undoubtedly lowers the chances of encountering data races due to their synchronized access design, which typically averts the peculiar crashes often seen with data races. However, the consistent use of actors is crucial to maintain this level of safety. It’s a common misconception that actors can completely eliminate data races; they reduce the risk, but do not abolish it entirely.

Consider this example where two asynchronous queues are interacting with an actor's data using `await`:

```swift
queueOne.async {
    await feeder.chickenStartsEating()
}
queueTwo.async {
    print(await feeder.numberOfEatingChickens)
}
```

The race condition is not about data being accessed simultaneously, but rather about the sequence of operations. We're left with two possible scenarios:

1. **Queue one is first**: It invokes `chickenStartsEating`, which increments the `numberOfEatingChickens`. Queue two then prints the number as 1.
2. **Queue two is first**: It prints `numberOfEatingChickens` before queue one has invoked `chickenStartsEating`, resulting in a printout of 0.

The key takeaway is that actors change the nature of the race condition rather than eliminating it. Instead of data being accessed mid-modification, leading to unpredictable states, the race is now about the order of operations. Although this is a more controlled and predictable scenario, it still requires careful consideration during the design of concurrent programs. By understanding the capabilities and limitations of actors, developers can better utilize them to write safer, more predictable concurrent code.


## Benchmarking

### Setup
To compare the performance, I have implemented two sets of code. One uses Swift's `actor` type to serialize access to a shared resource, and the other uses a `DispatchQueue`. Each piece of code measures the time taken to execute blocks of tasks involving temperature logging and calculates statistics such as the mean, median, and standard deviation of execution times.

[Actor Plaground Implementation](ActorTemperatureLogger.playground/Contents.swift)

[DispatchQueue Plaground Implementation](DispatchQueueTemperatureLogger.playground/Contents.swift)

### Results
The results are summarized in the following table and visualized in the accompanying graph:

| Runs | Component     | Average Execution Time (seconds) | Median Execution Time (seconds) | Standard Deviation of Execution Time (seconds) | Total Measurements | Notes |
|------|---------------|----------------------------------|---------------------------------|-------------------------------------------------|--------------------|-------|
| 10   | Actor         | 0.0263634085                     | 0.0302392705                    | 0.008733507339838242                           | 30                 |       |
| 10   | DispatchQueue | 0.038884270799999995             | 0.039969020999999993            | 0.003318502673248548                           | 30                 |       |
| 50   | Actor         | 0.09523081010000002              | 0.10296445800000001             | 0.023547593880998936                           | 150                |       |
| 50   | DispatchQueue | 0.19973209494                     | 0.214760354                     | 0.028667415804254786                           | 150                |       |
| 100  | Actor         | 0.21355324090000008              | 0.2293904585                    | 0.04365364316586947                            | 300                |       |
| 100  | DispatchQueue | 0.3505280370599999               | 0.308498854                     | 0.11525222904532295                            | 300                |       |
| 500  | Actor         | 1.41273607833                    | 1.46941725                      | 0.20757241215870095                            | 1500               |       |
| 500  | DispatchQueue | 1.4593390492419998               | 1.5291020835000002              | 0.7816940446783845                             | 1500               |       |
| 1000 | Actor         | 3.432818794544995                | 3.536968458                     | 0.44535471787905123                            | 3000               |       |
| 1000 | DispatchQueue | 3.0110555153670027               | 2.8920404165                    | 1.7202161787585477                             | 3000               | **     |
| 1500 | Actor         | 6.104391908370001                | 6.263336729500001               | 0.7372806404140805                             | 4500               |       |
| 1500 | DispatchQueue | 4.780818677598665                | 4.3577189165                    | 2.9351269876076653                             | 4500               | **     |
| 5000 | Actor         | 43.99566643877493                | 44.907944833                    | 4.778725795415856                              | 15000              |       |
| 5000 | DispatchQueue | 30.483703210767132               | 24.319241333                    | 24.598807693444005                             | 15000              | **    |

** Multiple errors encountered during runs.

* Errors: 
    * QueueTemperatureLogger(16217,0x16ef83000) malloc: double free for ptr 0x10f025000
    * QueueTemperatureLogger(16217,0x16ef83000) malloc: *** set a breakpoint in malloc_error_break to debug
    * Swift/ContiguousArrayBuffer.swift:600: Fatal error: Index out of range

* Ran on: Apple M2 Max - 64 ram

![Benchmark Graphic](benchmark.png)

From the graph and the table, we observe that as the execution count increases, the mean and standard deviation of execution times for both actors and queues increase, but actors tend to have a lower standard deviation, indicating a more consistent performance.


### Benchmark Observations and Stability vs. Performance
The benchmark results for 5000 interactions reveal a nuanced trade-off between the performance of dispatch queues and the stability offered by actors. While actors may exhibit a performance decrease under heavy load, they provide more predictable behavior, which is critical in production environments. This stability can outweigh raw performance benefits, especially when consistent state management and thread safety are prioritized. Future benchmarks could explore these trade-offs in depth, offering a more balanced view on when to use each model based on application needs.

### Discussing Actor Synchronization
The actor model in Swift uses mechanisms like mailboxing or message passing to synchronize access to its state. However, these mechanisms can introduce overhead, especially in complex scenarios with high contention. This aspect wasn't covered in the initial benchmarks and could be a topic for future exploration.


## Analysis
While both actors and queues manage concurrent executions efficiently, actors provide a structured way to handle concurrent access to shared resources, which can be easier to reason about and maintain. However, the performance varies based on the number of tasks and the nature of the work being done.

It is worth mentioning that the results obtained from benchmarks are highly contextual and should be interpreted with consideration of the specific tasks being performed.


## Conclusion
Embracing Swift's concurrency model, especially the use of actors, offers a sophisticated approach to managing concurrent operations. However, discernment is key; it's about selecting the tool that best aligns with your project's needs—balancing performance with the clarity and longevity of your codebase. Actors excel in scenarios demanding robust thread-safety and data integrity, although this might come with a trade-off in terms of performance overhead.

As Swift matures, its concurrency landscape also advances. Staying abreast of these developments is not just beneficial—it's essential for Swift developers aiming to craft applications that are not only powerful but are also resilient and efficient in the face of evolving requirements and multi-threading challenges.

## Reference to Swift's Actor Proposal
For readers interested in the theoretical underpinnings and formal introduction of actors in Swift, the [Swift Evolution proposal SE-0306](https://github.com/apple/swift-evolution/blob/main/proposals/0306-actors.md) is an indispensable resource.