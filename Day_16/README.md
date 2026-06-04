# Python Variables: Global and Local Variables

## Introduction

Variables are used to store data in Python. Based on where they are declared, variables are mainly of two types:

1. **Global Variables**
2. **Local Variables**

---

# Global Variable

A global variable is declared outside a function and can be accessed from anywhere in the program.

## Example

```python
global_var = 20

def fun():
    local_var = 10
    print(local_var)
    print(global_var)

fun()
```

### Output

```text
10
20
```

### Explanation

* `global_var` is declared outside the function.
* `local_var` is declared inside the function.
* Both variables can be accessed inside the function.

---

# Local Variable

A local variable is declared inside a function and can only be used within that function.

## Example

```python
xy = 100

def fun():
    xy = 101
    print(xy)

fun()
```

### Output

```text
101
```

### Explanation

* The local variable `xy = 101` is used inside the function.
* The global variable `xy = 100` remains unchanged.

---

# Printing Both Global and Local Variables

## Example

```python
xy = 100

def fun():
    xy = 101
    print("Local variable inside function:", xy)

fun()
print("Global variable outside function:", xy)
```

### Output

```text
Local variable inside function: 101
Global variable outside function: 100
```

### Explanation

* Inside the function, Python uses the local variable.
* Outside the function, Python uses the global variable.

---

# Modifying a Global Variable Using the global Keyword

The `global` keyword allows a function to modify a global variable.

## Example

```python
xy = 100

def fun():
    global xy
    xy = 200
    print(xy)

fun()
print(xy)
```

### Output

```text
200
200
```

### Explanation

* `global xy` tells Python to use the global variable.
* The value of `xy` is updated from `100` to `200`.

---

# Local Variable Takes Priority

## Example

```python
ab = 101

def fun():
    ab = 102
    print("Local variable:", ab)

fun()
```

### Output

```text
102
```

### Explanation

* The local variable `ab = 102` hides the global variable `ab = 101` inside the function.

---

# Using Local and Global Variables Inside a Function

## Example

```python
def fun():
    ab = 100
    global xy
    xy = 200

    print("Local variable:", ab)

fun()
print("Global variable:", xy)
```

### Output

```text
Local variable: 100
Global variable: 200
```

### Explanation

* `ab` is a local variable and exists only inside the function.
* `xy` is declared as global and can be accessed outside the function.

---

# Key Differences

| Global Variable                            | Local Variable                        |
| ------------------------------------------ | ------------------------------------- |
| Declared outside a function                | Declared inside a function            |
| Accessible throughout the program          | Accessible only within the function   |
| Can be modified using the `global` keyword | Exists only during function execution |
| Lifetime is the entire program             | Lifetime is limited to the function   |

---

# Summary

* Global variables are defined outside functions.
* Local variables are defined inside functions.
* Local variables have priority inside a function.
* Use the `global` keyword to modify a global variable from within a function.
* Understanding variable scope helps avoid bugs and makes code easier to maintain.


