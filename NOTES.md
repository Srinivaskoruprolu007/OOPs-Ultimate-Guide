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

## 3. Polymorphism

### What is Polymorphism?

- **Polymorphism** means "many forms." It allows an object of a subclass to be treated as an object of a superclass.
- The same method can behave differently based on the object it is called on.
- This allows for code flexibility, making it easier to extend and maintain.

### Key Concepts:

1. **Method Overloading**:

   - This refers to having multiple methods with the same name but different parameters. Python doesn't support traditional method overloading as seen in other languages like Java or C++, but it can be emulated by using default arguments or variable-length arguments.
2. **Method Overriding**:

   - In Python, subclasses can override methods of the parent class. This is the most common form of polymorphism.
   - The subclass provides a specific implementation of a method, even if the method has the same name in the parent class.

### Example Explanation:

In our example:

- We have a base class `Animal` with a method `sound()`, which is overridden in the subclasses `Dog`, `Cat`, and `Cow` to provide specific behaviors for each animal.
- The `make_sound()` function calls the `sound()` method on any `Animal` object, and the correct method is invoked depending on the type of the object (i.e., Dog, Cat, or Cow).
- This demonstrates **method overriding**, where the same method name behaves differently for different object types.

### Types of Polymorphism:

1. **Compile-time Polymorphism (Method Overloading)**:

   - Achieved by having multiple methods with the same name but different parameters (handled via default arguments or variable-length arguments in Python).
2. **Runtime Polymorphism (Method Overriding)**:

   - Achieved by overriding methods in subclasses. The method invoked is determined at runtime based on the object's type.

---

## 4. Encapsulation

### What is Encapsulation?

- **Encapsulation** is the mechanism of restricting direct access to some of an object's components, while providing controlled access through methods.
- It bundles data (attributes) and methods that operate on the data within a single unit (class), making the data secure from unauthorized access.

### Key Concepts:

1. **Private Attributes**:

   - Attributes prefixed with double underscores (`__`) are private to the class and cannot be accessed directly from outside the class.
   - These attributes are meant to be modified only through public methods.
2. **Public Methods**:

   - These methods provide controlled access to private attributes.
   - Methods like **getters** and **setters** are used to get or set the values of private attributes.
3. **Getter and Setter Methods**:

   - **Getters** are methods that allow reading the value of private attributes.
   - **Setters** are methods that allow modifying the value of private attributes but with certain conditions (e.g., validation).

### Example Explanation:

In our example:

- The `BankAccount` class has a private attribute `__balance` which is encapsulated.
- To interact with the balance, public methods `deposit()`, `withdraw()`, `get_balance()`, and `set_balance()` are provided.
- We cannot access the `__balance` directly from outside the class, ensuring that it is modified only through the provided methods.

### Why is Encapsulation Important?

- **Data Security**: By controlling how data is accessed and modified, we reduce the risk of data corruption.
- **Maintainability**: We can change the internal implementation of a class (e.g., how data is stored) without affecting the code that uses the class, as long as the public interface remains the same.
- **Flexibility**: We can easily add validation and other logic in setter methods to ensure data integrity.

---

## 5. Abstraction

### What is Abstraction?

Abstraction hides the implementation details of a system and shows only the necessary functionality to the user. It provides a way to interact with objects without knowing their internal workings.

### Key Concepts:

1. **Abstract Classes**:

   - Defined using the `ABC` module (`from abc import ABC`).
   - Cannot be instantiated directly.
   - Used to define common interfaces for derived classes.
2. **Abstract Methods**:

   - Declared using the `@abstractmethod` decorator.
   - Must be implemented in all concrete subclasses.
3. **Concrete Classes**:

   - Derived classes that implement all the abstract methods of an abstract class.

### Example Explanation:

In the provided example:

- The `Vehicle` class is abstract and defines the structure for vehicles.
- Both `Car` and `Motorcycle` implement the methods `start_engine()` and `stop_engine()` differently, while adhering to the interface defined by `Vehicle`.

### Why Use Abstraction?

- **Reusability**: Abstract classes define reusable interfaces for related objects.
- **Maintainability**: Changes in abstract classes propagate to derived classes, ensuring consistency.
- **Encapsulation**: It complements encapsulation by exposing only the relevant details to the user.

---

## 6. Modules

### What are Modules?

- A module in Python is a file containing Python definitions and statements.
- It allows you to organize and reuse code across multiple projects.

### Key Concepts:

1. **Importing Modules**:

   - Use `import module_name` to import the entire module.
   - Use `from module_name import function_name` to import specific functions.
2. **Creating a Custom Module**:

   - Save Python code in a `.py` file, and you can import and use it like any other module.
   - Example: `math_utils.py` is a custom module for mathematical operations.
3. **Standard Library Modules**:

   - Python has built-in modules for file handling (`os`, `shutil`), data handling (`csv`, `json`), etc.
   - Example: `import os` gives access to file system operations.
4. **Third-Party Modules**:

   - Install external libraries using `pip` (e.g., `numpy`, `pandas`).
   - Example: `import numpy as np` for working with arrays.
5. **Module Aliases**:

   - You can use `as` to create a shortcut for module names.
   - Example: `import numpy as np` makes `numpy` accessible as `np`.
6. **Module Functions**:

   - Define functions in your module and use them in any script.
   - Example: `add(a, b)` in `math_utils.py`.
7. **Executing Code in Modules**:

   - Code outside functions in a module is executed when imported.
   - Use the `if __name__ == "__main__":` condition to test or execute code only when the module is run directly.

### Example Code:

Refer to the **Module Demo**: [module_demo.py](examples/module_demo.py) for how to create and use custom modules.

### Notes:

- Use modules to keep your code organized and modular.
- Ensure modules are small and focused on a single task (Single Responsibility Principle).
- Use `__init__.py` for package initialization when creating Python packages.

### Advantages of Using Modules:

- **Reusability**: You can use the same code in multiple projects without rewriting it.
- **Maintainability**: It's easier to manage smaller code files rather than a huge, monolithic script.
- **Namespace**: Modules provide their own namespace, avoiding naming conflicts between different parts of the program.

---

## 7. File Handling 

### Key Operations:

1. **Writing to a File**:

   - Use the `open(file_name, 'w')` mode to create/overwrite a file.
   - Use the `write()` method to write content to the file.
2. **Reading from a File**:

   - Use the `open(file_name, 'r')` mode to read a file.
   - Use the `read()` or `readlines()` method to retrieve content.
3. **Appending to a File**:

   - Use the `open(file_name, 'a')` mode to add content to the end of the file without overwriting existing content.

### Notes:

- Always use the `with` statement to handle files to ensure proper closure.
- Handle exceptions like `FileNotFoundError` for better reliability.
- Avoid hardcoding file paths; use libraries like `os` or `pathlib` for dynamic paths.
