# Python - Test-driven development

## 📚 Description

This project focuses on **Test-Driven Development (TDD)** in Python using:
- `doctest` for inline documentation and functional testing.
- `unittest` for structured and modular test cases.
- `pycodestyle` for code style compliance (PEP8).
- Exception handling and input validation.

---

## 🧪 Functional Tests (`doctest`)

All `.py` modules include embedded test cases inside `.txt` files located in the `tests/` folder.  
These tests are run using the following command:

```bash
python3 -m doctest ./tests/*
```

### Doctest Files:

| Module                  | Doctest File                 |
|-------------------------|------------------------------|
| `add_integer.py`        | `tests/0-add_integer.txt`     |
| `matrix_divided.py`     | `tests/2-matrix_divided.txt`  |
| `say_my_name.py`        | `tests/3-say_my_name.txt`     |
| `print_square.py`       | `tests/4-print_square.txt`    |
| `text_indentation.py`   | `tests/5-text_indentation.txt`|

---

## 🧪 Unit Tests (`unittest`)

A complete test suite was written using the `unittest` module for the function:

```python
def max_integer(list=[])
```

The test file is located in:

```bash
tests/6-max_integer_test.py
```

Run it with:

```bash
python3 -m unittest tests.6-max_integer_test
```

Test cases include:
- Sorted and unsorted lists
- Negative numbers
- Floats
- Strings
- Empty list
- Invalid types

---

## 🧼 Code Style

All `.py` files conform to **PEP8** standards.

To check:

```bash
pycodestyle *.py
```

No lines exceed 79 characters and each file ends with a newline.

---

## 📌 Docstrings

Each `.py` file contains:
- A **module docstring**
- A **function docstring**

You can test this with:

```bash
python3 -c 'print(__import__("module_name").__doc__)'
python3 -c 'print(__import__("module_name").function_name.__doc__)'
```

⚠️ For files starting with a number (e.g., `0-add_integer.py`), use this workaround:

```python
import importlib.util
spec = importlib.util.spec_from_file_location("mod", "./0-add_integer.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
print(mod.__doc__)
print(mod.add_integer.__doc__)
```

---

## 📁 File Overview

| File                     | Purpose                           |
|--------------------------|------------------------------------|
| `add_integer.py`         | Adds two integers with validation |
| `matrix_divided.py`      | Divides all elements of a matrix  |
| `say_my_name.py`         | Prints a full name                |
| `print_square.py`        | Prints a square using `#`         |
| `text_indentation.py`    | Adds line breaks after punctuation|
| `6-max_integer.py`       | Returns the max integer in a list |
| `tests/*.txt`            | `doctest` test files              |
| `tests/6-max_integer_test.py` | `unittest` test class for `max_integer` |

---

## ✅ Skills

- Write robust, tested Python code
- Build tests before implementation (TDD approach)
- Handle input types and raise meaningful exceptions
- Maintain clean, readable, and PEP8-compliant code

---

## 🏁 Author
Made By Sofian Messaoui
Thanks to all my peers of the cohort C26 of Holberton School at Toulouse

Made as part of Holberton School's Higher Level Programming curriculum.