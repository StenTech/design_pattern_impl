# design_pattern_impl

a collection af design pattrens implementation in python.

## 1. Singleton

implementing singleton pattern in python. the singleton pattern is a creational pattern that ensures that only one object of a particular class is ever created. all further references to objects of the singleton class refer to the same underlying instance.
> the first two implementations are the best practice for implementing singleton pattern in python. the third implementation is not recommended.

## 2. Factory

implementing factory pattern in python. the factory pattern is a creational pattern that uses factory methods to deal with the problem of creating objects without having to specify the exact class of the object that will be created. this is done by creating objects by calling a factory method—either specified in an interface and implemented by child classes, or implemented in a base class and optionally overridden by derived classes—rather than by calling a constructor.

## 3. Observer

implementing observer pattern in python. the observer pattern is a behavioral design pattern that defines a one-to-many dependency between objects so that when one object changes state, all of its dependents are notified and updated automatically.

## 4. Strategy

implementing strategy pattern in python. the strategy pattern is a behavioral design pattern that lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable.

## 5. Command

implementing command pattern in python. the command pattern is a behavioral design pattern in which an object is used to encapsulate all information needed to perform an action or trigger an event at a later time. this information includes the method name, the object that owns the method and values for the method parameters. the command pattern allows for loosely coupled systems by separating objects that issue a request from the objects that actually process the request. these requests are called events and the code that processes the requests are called event handlers.
in our code, we implement the execution and the undo of the command. the execution of the command is done by calling the execute method. the undo of the command is done by calling the undo method. but we can also implement the redo of the command by calling the redo method.