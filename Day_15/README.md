# Python Functions - Beginner Guide

## Introduction

A **function** is a block of code that performs a specific task. Functions help make programs organized, reusable, and easier to understand.

Functions are defined using the `def` keyword and can be called whenever needed.

---

# 1. Simple Function Example

This function prints a message when called.

```python
def myfun():
    print("Hello learn python step by step")

myfun()
```

### Output

```text
Hello learn python step by step
```

---

# 2. Function with Parameter

Parameters allow values to be passed into a function.

```python
def myfun(name):
    print("Hello", name)

myfun("Shiv")
```

### Output

```text
Hello Shiv
```

### Explanation

* `def` is used to define a function.
* `myfun` is the function name.
* `name` is a parameter that receives the value passed during the function call.

---

# 3. Addition of Two Numbers Using Function

```python
def cal(a, b):
    return a + b

result = cal(10, 20)
print(result)
```

### Output

```text
30
```

### Explanation

* `a` and `b` are parameters.
* `return` sends the result back to the caller.

---

# 4. Function Returning No Value

```python
def fun():
    return

print(fun())
```

### Output

```text
None
```

### Explanation

When a function does not return a value, Python automatically returns `None`.

---

# 5. Function Without Return Statement

```python
def fun():
    i = 10

print(fun())
```

### Output

```text
None
```

### Explanation

Since there is no `return` statement, the function returns `None`.

---

# 6. Function Returning a Value

```python
def fun():
    i = 10
    return i

print(fun())
```

### Output

```text
10
```

---

# 7. Printing Value Inside Function

```python
def fun():
    i = 100000
    print(i)

fun()
```

### Output

```text
100000
```

### Explanation

The value is printed directly inside the function instead of being returned.

---

# 8. Addition Using Print Statement

```python
def cal(a, b):
    print(a + b)

cal(2, 5)
```

### Output

```text
7
```

---

# 9. Addition Using Return Statement

```python
def cal(a, b):
    return a + b

print(cal(2, 3))
```

### Output

```text
5
```

---

# Key Concepts

| Concept   | Description                                       |
| --------- | ------------------------------------------------- |
| Function  | A reusable block of code that performs a task     |
| def       | Keyword used to define a function                 |
| Parameter | Variable that receives data in a function         |
| Argument  | Actual value passed to a function                 |
| return    | Sends a value back from a function                |
| None      | Default value returned when no value is specified |

---

# Benefits of Functions

* Code reusability
* Better organization
* Easier maintenance
* Improved readability
* Reduced code duplication

---

# Conclusion

Functions are one of the most important concepts in Python programming. They help divide large programs into smaller, manageable pieces of code and allow developers to reuse logic efficiently.
