# Streamline Your Testing with SimpleMock Swift: The Lightweight and Simple Mock Implementation You Need

Testing is an essential part of any software development project. However, testing can be time-consuming and complex, especially when it comes to mocking objects for unit tests. That’s where SimpleMock Swift comes in. It is a lightweight and simple mock implementation that can help you create your own mocks easily and quickly.

Creating mocks from scratch can be tricky and sometimes you don’t want to use a complex tool just to test simple cases. The idea of this repository is more to show how you can create your own mock than just depend on external tools. When you write your own mocks, you aren’t using reflection, so your mocks will almost always be extremely fast.

[SimpleMock Swift](https://github.com/Tavernari/SimpleMock) provides a basic structure for defining and managing mock objects. Your object mock has to conform to the Mock protocol and set an Enum with cases representing methods you expect to use. After defining the methods, you must create the collections that will store expectations, resolvers, and interactions. On the methods the system under testing will use, you should call resolve to register interaction and request the value that should return.

Here’s an example of how to use SimpleMock Swift to create a mock for a service:

```swift
class ServiceMock: Service, Mock { 

  enum Methods: Hashable { 

    case save(_ id: String, _value: Int) 
    case load(_ id: String) 
  } 

  var methodsResolvers: [[Methods] : Resolver] = [:]
  var methodsExpected: [[Methods]] = [] 
  var methodsRegistered: [[Methods]] = [] 
  
  func save(_id: String, _ value: Int) throws { 
  
    return try self.resolve(method: .save(id, value)) 
  }
  
  func load(_ id: String) throws -> Int { 

    return try self.resolve(method: .load(id)) 
  } 
}
```

In this example, we are creating a mock object for a service. The mock object conforms to the Mock protocol and defines an Enum called Methods with cases representing the methods we expect to use. The methodsResolvers, methodsExpected, and methodsRegistered properties are collections that store expectations, resolvers, and interactions.
Here’s an example of how to use SimpleMock 

Swift to test the service:

```swift
try serviceMock.expect(method: .load(self.id)) { 0 } 
try serviceMock.expect(method: .save(self.id, 10)) { Void() } 
try serviceMock.expect(method: .load(self.id), after: .save(self.id, 10)) { 10 } 

XCTAssertEqual(try serviceMock.load(self.id), 0) 
XCTAssertNoThrow(try serviceMock.save(self.id, 10)) 
XCTAssertEqual(tryserviceMock.load(self.id), 10) 
XCTAssertNoThrow(try self.serviceMock.verify())
```

In this example, we are setting expectations for the load and save methods of the service mock object. We then call the methods and assert that the results are what we expect. Finally, we verify that all the expectations were met.

## Conclusion

In conclusion, SimpleMock is a lightweight and easy-to-use mock implementation that can help you create your own mocks easily and quickly. Whether you’re working on a small personal project or a large-scale application, SimpleMock Swift can streamline your testing process and help you achieve better code coverage.


https://github.com/Tavernari/SimpleMock