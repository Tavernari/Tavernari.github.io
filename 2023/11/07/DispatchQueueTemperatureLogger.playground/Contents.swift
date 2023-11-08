import Foundation

class ExecutionTimeTracker {
    private let queue = DispatchQueue(label: "test.ExecutionTimeTracker")
    private var executionTimes: [Double] = []

    func addExecutionTime(_ time: Double) {
        queue.sync {
            executionTimes.append(time)
        }
    }
    
    func calculateStatistics(completion: @escaping (_ mean: Double, _ median: Double, _ standardDeviation: Double) -> Void) {
        queue.async {
            let mean = self.executionTimes.reduce(0, +) / Double(self.executionTimes.count)
            let sortedTimes = self.executionTimes.sorted()
            let median = sortedTimes.count % 2 == 0 ?
                (sortedTimes[sortedTimes.count / 2 - 1] + sortedTimes[sortedTimes.count / 2]) / 2 :
                sortedTimes[sortedTimes.count / 2]
            let sumOfSquaredAvgDiff = self.executionTimes.map { pow($0 - mean, 2.0) }.reduce(0, +)
            let standardDeviation = sqrt(sumOfSquaredAvgDiff / Double(self.executionTimes.count))
            
            completion(mean, median, standardDeviation)
        }
    }
}

class TemperatureLogger {
    private var measurements: [Int] = []
    private let queue = DispatchQueue(label: "test.TemperatureLogger")

    func log(temperature: Int) {
        queue.sync {
            measurements.append(temperature)
        }
    }
    
    func averageTemperature(completion: @escaping (Int) -> Void) {
        queue.async {
            let average = self.measurements.reduce(0, +) / self.measurements.count
            completion(average)
        }
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
    let blockStart = DispatchTime.now()
    DispatchQueue.global().async {
        logger.log(temperature: Int.random(in: 60...80))
        logger.log(temperature: Int.random(in: 60...80))
        logger.log(temperature: Int.random(in: 60...80))
        logger.averageTemperature { average in
            let blockEnd = DispatchTime.now()
            let nanoTime = blockEnd.uptimeNanoseconds - blockStart.uptimeNanoseconds
            let timeInterval = Double(nanoTime) / 1_000_000_000
            timeTracker.addExecutionTime(timeInterval)
            group.leave()
        }
    }
}

group.notify(queue: .main) {
    timeTracker.calculateStatistics { mean, median, standardDeviation in
        print("Average execution time: \(mean) seconds")
        print("Execution time median: \(median) seconds")
        print("Execution time standard deviation: \(standardDeviation) seconds")
        print("Total measurements: \(logger.totalOfMeasurements())")
    }
}

