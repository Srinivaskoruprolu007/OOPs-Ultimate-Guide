# OOPs Ultimate Guide - Notes

## 1. Classes and Objects

### What is a Class?

- A **class** is a blueprint for creating objects (instances).
- A class defines properties (attributes) and behaviors (methods) that the objects created from the class will have.
- In Python, a class is defined using the `class` keyword.

### What is an Object?

- An **object** is an instance of a class.
- When a class is defined, no memory is allocated. When an object is instantiated from the class, the memory is allocated.
- Objects represent real-world entities in a program.

### Example Explanation:

In our example, we created a `Dog` class:

- The `__init__()` method is a special method called the **constructor**. It is used to initialize the object's attributes when a new object is created.
- We defined two attributes: `name` and `breed`, which represent the dog's name and breed.
- The `bark()` method is a regular function that is used to make the dog "bark."

When we create objects like `dog1 = Dog("Buddy", "Golden Retriever")`, we're instantiating the `Dog` class and assigning the values to the attributes. We then use the `bark()` method to make the dog "bark."

---

### Key Points to Remember:

- **Class Definition**: Use the `class` keyword to define a class.
- **Attributes**: Variables defined inside a class to hold values specific to the object.
- **Methods**: Functions defined inside a class to perform actions on the object.
- **Constructor (`__init__`)**: Initializes the object's attributes when an instance is created.

---

## 2. Inheritance

### What is Inheritance?

- **Inheritance** is a mechanism in OOP that allows a class to inherit attributes and methods from another class.
- It promotes **code reuse** and creates a hierarchical relationship between classes.
- In Python, inheritance is implemented by creating a child class that inherits from a parent class.

### Parent Class and Child Class:

- A **parent class** (also called a **base class**) defines common attributes and methods.
- A **child class** (also called a **subclass**) inherits from the parent class, allowing it to access its attributes and methods.
- The child class can override methods of the parent class to provide specialized behavior.

### Key Concepts:

1. **`super()`**: A function used in the child class to call methods and constructors from the parent class.
2. **Method Overriding**: When a method in the child class has the same name as one in the parent class, the child class's version "overrides" the parent class's version.
3. **Abstract Methods**: These are methods in a parent class that are meant to be implemented by the child class.

### Example Explanation:

In our example:

- The `Animal` class is the parent class with a method `speak()`, which we expect to be implemented by subclasses like `Dog` and `Cat`.
- The `Dog` and `Cat` classes inherit from `Animal` and provide their own version of the `speak()` method.
- By using inheritance, we avoid code duplication and maintain a clear hierarchy of classes.

### Types of Inheritance:

1. **Single Inheritance**: A class inherits from one parent class (as shown in the example).
2. **Multiple Inheritance**: A class inherits from more than one parent class.
3. **Multilevel Inheritance**: A class inherits from a class that has already inherited from another class.
4. **Hierarchical Inheritance**: Multiple classes inherit from a single parent class.
5. **Hybrid Inheritance**: A combination of multiple inheritance types.

---

## 3. Polymorphism (Coming Soon)

- **Polymorphism** allows objects of different classes to be treated as objects of a common superclass. It also allows methods to do different things based on the object it is acting upon.
- We'll cover **Method Overloading** and **Method Overriding** in this section.

---

## 4. Encapsulation (Coming Soon)

- **Encapsulation** is the concept of bundling data (attributes) and methods that operate on the data into a single unit (class).
- We'll also discuss the use of **private** and **public** access modifiers.

---

## 5. Abstraction (Coming Soon)

- **Abstraction** is the concept of hiding complex implementation details and showing only the necessary functionality to the user.
- We’ll explore abstract classes and methods.

---

## 6. Modules (Coming Soon)

- Python allows you to create **modules** to organize code logically. We'll explore how to import and use modules in Python.
- We’ll create and import custom modules in this section.

---

## 7. File Handling (Coming Soon)

- File handling allows you to read from and write to files in Python.
- We’ll cover how to open, read, write, and close files.
- Examples will include reading and writing to text files, as well as using JSON for data storage.
