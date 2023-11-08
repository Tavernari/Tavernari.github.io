import Foundation

actor ExecutionTimeTracker {
    private var executionTimes: [Double] = []

    func addExecutionTime(_ time: Double) {
        executionTimes.append(time)
    }
    
    func calculateStatistics() -> (mean: Double, median: Double, standardDeviation: Double) {
        let mean = executionTimes.reduce(0, +) / Double(executionTimes.count)
        let sortedTimes = executionTimes.sorted()
        let median = sortedTimes.count % 2 == 0 ?
            (sortedTimes[sortedTimes.count / 2 - 1] + sortedTimes[sortedTimes.count / 2]) / 2 :
            sortedTimes[sortedTimes.count / 2]
        let sumOfSquaredAvgDiff = executionTimes.map { pow($0 - mean, 2.0) }.reduce(0, +)
        let standardDeviation = sqrt(sumOfSquaredAvgDiff / Double(executionTimes.count))
        
        return (mean, median, standardDeviation)
    }
}

actor TemperatureLogger {
    private var measurements: [Int] = []
    
    func log(temperature: Int) {
        measurements.append(temperature)
    }
    
    func averageTemperature() -> Int {
        guard !measurements.isEmpty else { return 0 }
        return measurements.reduce(0, +) / measurements.count
    }
    
    func totalOfMeasurements() -> Int { measurements.count }
}

// Usage
let logger = TemperatureLogger()
let timeTracker = ExecutionTimeTracker()
let group = DispatchGroup()
let total = 100

for _ in 1...total {
    group.enter()
    Task {
        let blockStart = DispatchTime.now()
        await logger.log(temperature: Int.random(in: 60...80))
        await logger.log(temperature: Int.random(in: 60...80))
        await logger.log(temperature: Int.random(in: 60...80))
        let _ = await logger.averageTemperature()
        let blockEnd = DispatchTime.now()
        let nanoTime = blockEnd.uptimeNanoseconds - blockStart.uptimeNanoseconds
        let timeInterval = Double(nanoTime) / 1_000_000_000
        await timeTracker.addExecutionTime(timeInterval)
        group.leave()
    }
}

group.notify(queue: .main) {
    Task {
        let stats = await timeTracker.calculateStatistics()
        print("Average execution time: \(stats.mean) seconds")
        print("Execution time median: \(stats.median) seconds")
        print("Execution time standard deviation: \(stats.standardDeviation) seconds")
        let total = await logger.totalOfMeasurements()
        print("Total measurements: \(total)")
    }
}
