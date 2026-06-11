# Python OOPs Inheritance Examples

This repository contains simple Python programs demonstrating the different types of **Inheritance** in Object-Oriented Programming (OOP).

## What is Inheritance?

Inheritance is an OOP concept where one class (child/subclass) acquires the properties and methods of another class (parent/superclass).

### Benefits of Inheritance

* Code reusability
* Easy maintenance
* Improved readability
* Supports hierarchical classification
* Reduces code duplication

---

# Types of Inheritance

1. Single Inheritance
2. Multilevel Inheritance
3. Hierarchical Inheritance
4. Multiple Inheritance

---

## 1. Single Inheritance

A child class inherits from a single parent class.

### Example

```python
class A:
    def m1(self):
        print("This is m1 method from class A")

class B(A):
    def m2(self):
        print("This is m2 method from class B")

obj = B()
obj.m1()
obj.m2()
```

### Output

```text
This is m1 method from class A
This is m2 method from class B
```

---

## Single Inheritance – Mathematical Operations

```python
class A:
    x, y = 10, 20

    def m1(self):
        print(self.x + self.y)

class B(A):
    a, b = 70, 20

    def m2(self):
        print(self.a - self.b)

obj = B()
obj.m1()
obj.m2()
```

### Output

```text
30
50
```

---

## 2. Multilevel Inheritance

A class inherits from another child class, forming a chain.

### Structure

```text
A → B → C
```

### Example

```python
class A:
    x, y = 11, 10

    def m1(self):
        print(self.x + self.y)

class B(A):
    a, b = 12, 7

    def m2(self):
        print(self.a - self.b)

class C(B):
    i, j = 3, 2

    def m3(self):
        print(self.i * self.j)

obj = C()
obj.m1()
obj.m2()
obj.m3()
```

### Output

```text
21
5
6
```

---

## 3. Hierarchical Inheritance

Multiple child classes inherit from a single parent class.

### Structure

```text
      A
    / | \
   B  C  D
```

### Example

```python
class A:
    x, y = 10, 20

    def m1(self):
        print(self.x + self.y)

class B(A):
    a, b = 20, 11

    def m2(self):
        print(self.a - self.b)

class C(A):
    d, e = 5, 7

    def m3(self):
        print(self.d * self.e)

class D(A):
    i, j = 10, 2

    def m4(self):
        print(self.i / self.j)
```

### Important Note

* `B`, `C`, and `D` all inherit from `A`.
* `B`, `C`, and `D` are sibling classes.
* An object of `D` can access:

  * Methods defined in `D`
  * Methods inherited from `A`
* An object of `D` **cannot directly access** methods that belong only to `B` or `C`.

### Incorrect Usage

```python
obj = D()

obj.m1()   # Valid
obj.m2()   # Error
obj.m3()   # Error
obj.m4()   # Valid
```

### Error

```text
AttributeError: 'D' object has no attribute 'm2'
```

### Correct Usage

Create separate objects for each child class.

```python
obj = B()
obj.m1()
obj.m2()

obj = C()
obj.m3()

obj = D()
obj.m4()
```

### Output

```text
30
9
35
5.0
```

---

## 4. Multiple Inheritance

A child class inherits from more than one parent class.

### Structure

```text
    A     B     C
     \    |    /
          D
```

### Example

```python
class A:
    x, y = 10, 20

    def m1(self):
        print(self.x + self.y)

class B:
    a, b = 12, 10

    def m2(self):
        print(self.a - self.b)

class C:
    i, j = 3, 5

    def m3(self):
        print(self.i * self.j)

class D(A, B, C):
    c, d = 10, 2

    def m4(self):
        print(self.c / self.d)

obj = D()

obj.m1()
obj.m2()
obj.m3()
obj.m4()
```

### Output

```text
30
2
15
5.0
```

---

# Summary

| Inheritance Type         | Description                               |
| ------------------------ | ----------------------------------------- |
| Single Inheritance       | One child inherits from one parent        |
| Multilevel Inheritance   | Child inherits from another child class   |
| Hierarchical Inheritance | Multiple children inherit from one parent |
| Multiple Inheritance     | One child inherits from multiple parents  |

---

## Author

Python OOPs Inheritance Examples for learning and practice.

Happy Coding! 🚀
