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

<div style="display: flex; justify-content: center;">
  <img src="./icon.webp" style="height: 200px;" />
</div>

## Say Goodbye to Clunky String Searches with StringContainsOperators

If you’ve ever needed to search for multiple substrings within a larger string in Swift, you know it can be a pain. Checking if a string contains one or more substrings often requires writing multiple lines of code, which can quickly become unwieldy and difficult to maintain. But what if there was a better way? That’s where `StringContainsOperators` comes in.

### The Problem with Native String Searching

Swift’s built-in contains method is great for checking if a single substring exists within a larger string. However, when searching for multiple substrings, things can get messy quickly. You might find yourself writing something like this:

```swift
let text = "The quick brown fox jumps over the lazy dog."

let containsQuickAndJumps = text.contains("quick") && text.contains("jumps")
let containsFoxOrDog = text.contains("fox") || text.contains("dog")
```

While this example is relatively simple, imagine having to check for a dozen or more substrings using this approach. The code becomes increasingly complex and harder to read, making it a breeding ground for bugs.

### Introducing StringContainsOperators

`StringContainsOperators` is a Swift library that simplifies searching for multiple substrings within a given text. It provides custom infix operators and predicates, enabling you to create complex and flexible search patterns in a more readable and concise manner.

Here’s an example of how you can use `StringContainsOperators` to search for substrings in your text:

```swift
import `StringContainsOperators`

let text = "The quick brown fox jumps over the lazy dog."

// Check if text contains "quick" OR "jumps"
let result1 = text.contains("quick" || "jumps")
print(result1) // true

// Check if text contains "fox" AND "dog"
let result2 = text.contains("fox" && "dog")
print(result2) // true

// Check if text contains "fox" AND ("jumps" OR "swift")
let result3 = text.contains("fox" && ("jumps" || "swift"))
print(result3) // true
```

As you can see, `StringContainsOperators` allows you to express complex search patterns in a much more readable and intuitive way. You no longer need to repeatedly call the contains method or chain multiple logical operators together.

### Comparing Native Approach and `StringContainsOperators`

Let’s take a closer look at the differences between the native approach and `StringContainsOperators` when checking for multiple substrings.

#### Native Approach

```swift
let text = "The quick brown fox jumps over the lazy dog."

let containsQuickOrJumps = text.contains("quick") || text.contains("jumps")
let containsFoxAndDog = text.contains("fox") && text.contains("dog")
let containsFoxAndJumpsOrSwift = text.contains("fox") && (text.contains("jumps") || text.contains("swift"))
```

#### StringContainsOperators

```swift
import `StringContainsOperators`

let text = "The quick brown fox jumps over the lazy dog."

let containsQuickOrJumps = text.contains("quick" || "jumps")
let containsFoxAndDog = text.contains("fox" && "dog")
let containsFoxAndJumpsOrSwift = text.contains("fox" && ("jumps" || "swift"))
```

In both examples, we’re trying to accomplish the same goal: checking if the text contains specific substrings based on different conditions. However, the `StringContainsOperators` example is more concise, expressive, and easier to read. The custom infix operators allow you to describe the search patterns more naturally, making it simpler to understand the code at a glance.

https://github.com/Tavernari/`StringContainsOperators`

### In Conclusion

`StringContainsOperators` is a powerful and elegant solution to the problem of searching for multiple substrings in Swift. It simplifies the process, making your code more readable and maintainable. Say goodbye to clunky and complex string search code, and give `StringContainsOperators` a try. It could be the key to unlocking a cleaner and more efficient way of handling string searches in your Swift projects.