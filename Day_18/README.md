# Python OOPs Basics

## Introduction

This project demonstrates the basic concepts of Object-Oriented Programming (OOP) in Python using classes and objects.

### Key Points

* Python supports both **Procedural Programming** and **Object-Oriented Programming (OOP)**.
* Programs can be written with or without classes in Python.
* A **Class** is a blueprint for creating objects.
* An **Object** is an instance of a class.

---

# 1. Creating a Class

```python
class myclass:
    x = 5

print(myclass)
```

### Description

* A class named `myclass` is created.
* It contains a class variable `x` with value `5`.
* Printing the class displays information about the class object.

---

# 2. Creating a Class with an Object

```python
class myclass:
    x = 5

print(myclass)

p1 = myclass()
print(p1.x)
```

### Description

* A class `myclass` is created.
* An object `p1` is created from the class.
* The value of variable `x` is accessed using the object.

### Output

```text
5
```

---

# 3. Creating Methods Inside a Class

```python
class myclass:
    def myfun(self):
        pass

    def display(self):
        print("Shiv is doing coding")

mc = myclass()
mc.myfun()
mc.display()
```

### Description

* `myfun()` is an empty method using `pass`.
* `display()` prints a message.
* An object `mc` is created and methods are called using the object.

### Output

```text
Shiv is doing coding
```

---

# 4. Printing a Message Using Class and Object

```python
class myclass:
    def fun(self):
        print("Hello Oops concept in python")

m = myclass()
m.fun()
```

### Description

* A method `fun()` is defined inside the class.
* The method prints a message when called through an object.

### Output

```text
Hello Oops concept in python
```

---

# Conclusion

This project covers:

* Creating classes
* Creating objects
* Defining methods
* Calling methods using objects
* Basic understanding of Python OOP concepts
