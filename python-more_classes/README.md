# Python - More Classes and Objects

This project explores object-oriented programming (OOP) in Python by implementing a `Rectangle` class. The project is designed to gradually introduce class attributes, instance methods, special methods, static methods, and class methods.

## 📁 Project Structure

This repository is organized into a single class file (`rectangle.py`) that evolves through multiple tasks, each building upon the previous one.

## ✅ Features

The `Rectangle` class includes the following features:

- **Private Attributes**
  - `__width`: validated as an integer >= 0
  - `__height`: validated as an integer >= 0

- **Instance Methods**
  - `area()`: returns the area of the rectangle
  - `perimeter()`: returns the perimeter, or 0 if width or height is 0

- **Special Methods**
  - `__str__()`: prints the rectangle using the `print_symbol`
  - `__repr__()`: returns a string representation that can recreate the object
  - `__del__()`: prints a message when an instance is deleted

- **Class Attributes**
  - `number_of_instances`: tracks how many instances of the class exist
  - `print_symbol`: customizable symbol used in the string representation

- **Static Method**
  - `bigger_or_equal(rect_1, rect_2)`: returns the rectangle with the greater area

- **Class Method**
  - `square(size=0)`: returns a new Rectangle instance with width and height equal to `size`

## 📜 Usage Example

```python
from rectangle import Rectangle

r1 = Rectangle(3, 4)
r2 = Rectangle.square(5)

print(r1.area())            # 12
print(r2)                   # prints a 5x5 square using '#'
print(Rectangle.number_of_instances)  # tracks number of live objects

print(Rectangle.bigger_or_equal(r1, r2))  # returns r2