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

## 2. Inheritance (Coming Soon)

- **Inheritance** allows a class to inherit properties and methods from another class. This promotes code reuse and is one of the key concepts in OOP.
- We'll cover **Single Inheritance**, **Multiple Inheritance**, and **Method Overriding**.

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
