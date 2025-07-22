![Python Memory and Object Identity](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*ncy1CS4YXZFYZu_YCoUN8g.png)

# Everything is Object in Python 🧠🐍

Python is often praised for being simple and readable, but under the hood, it has a very powerful and sometimes subtle object model. In this blog post, I’ll summarize what I learned while completing the “Everything is Object” project at Holberton School. This project helped me understand how Python handles identity, mutability, and object references—key concepts for writing efficient and bug-free code.

## 🆔 `id` and `type`: Understanding the Basics

In Python, everything is an object. That means integers, strings, lists, even functions—are all instances of objects. You can verify what type an object is using the `type()` function, and you can get the unique identifier (essentially the memory address in CPython) using the `id()` function.

```python
a = 42
print(type(a))  # <class 'int'>
print(id(a))    # 9794400 (example, depends on system)
```

These tools help you understand how Python tracks and manages variables in memory.

## 🌀 Mutable vs Immutable Objects

An immutable object is one that cannot be changed after it is created. Examples include `int`, `float`, `str`, and `tuple`.

```python
a = 10
print(id(a))  # e.g., 9793376
a += 1
print(id(a))  # different ID → new object
```

A mutable object can be changed in place. Examples include `list`, `dict`, and `set`.

```python
l = [1, 2, 3]
print(id(l))
l.append(4)
print(id(l))  # same ID → modified in place
```

## 🔁 Why It Matters: Python's Internal Behavior

Understanding the difference between mutable and immutable objects is crucial. Python treats them differently when performing operations or assigning values. With mutable objects, changes affect all references to that object. With immutable ones, changes result in new objects.

```python
# Immutable
a = 10
b = a
a += 1
print(b)  # 10

# Mutable
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)  # [1, 2, 3, 4]
```

## 🧪 Function Arguments: Call by Object Reference

Python uses "call by object reference" (or "call by sharing"). This means function arguments are passed as references to objects, not copies.

With immutable objects:

```python
def increment(n):
    n += 1

a = 10
increment(a)
print(a)  # 10
```

With mutable objects:

```python
def mutate(l):
    l.append(4)

my_list = [1, 2, 3]
mutate(my_list)
print(my_list)  # [1, 2, 3, 4]
```

The takeaway: functions can modify mutable objects passed as arguments, but not immutable ones.

## 🧠 Advanced Tasks: Interning, Tuples, Copying

Some Python objects are interned (shared in memory) for efficiency, like small integers and empty tuples.

```python
a = ()
b = ()
print(a is b)  # True

x = 1000
y = 1000
print(x is y)  # False (likely)
```

A common source of confusion: single-element tuples.

```python
a = (1)
print(type(a))  # <class 'int'>

b = (1,)
print(type(b))  # <class 'tuple'>
```

To copy a list safely (not just create a new reference), use slicing:

```python
def copy_list(a_list):
    return a_list[:]
```

This ensures the original list remains unchanged when the copy is modified.

## ✅ Conclusion

This project helped me understand Python's object model more deeply. I learned how memory works, how Python handles object identity and mutability, and why `is` and `==` are not the same. It also showed me how functions interact with object references, and how to safely manage state with mutable types. These concepts are foundational for writing clean, efficient, and predictable Python code.