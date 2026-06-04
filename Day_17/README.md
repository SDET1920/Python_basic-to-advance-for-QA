# 🐍 Python Functions & Arguments (Complete Notes)

## 📌 Introduction

In Python, a function can accept different types of arguments (parameters). These help pass values into functions in different ways.

There are mainly **two types of arguments**:

1. Positional Arguments
2. Keyword Arguments

---

# 1️⃣ Positional Arguments

In positional arguments, values are assigned based on their position.

## Example

```python
def fun(i, j):
    print(i, j)

fun(10, 20)
```

### Output

```text
10 20
```

### Explanation

* `10` → assigned to `i`
* `20` → assigned to `j`
* Order matters in positional arguments

---

# 2️⃣ Keyword Arguments

In keyword arguments, values are assigned using parameter names.

## Example

```python
def fun(i, j):
    print(i, j)

fun(i=11, j=12)
```

### Output

```text
11 12
```

### Explanation

* Values are passed with parameter names
* Order does NOT matter

---

# 3️⃣ Default Arguments

Default arguments provide a default value if no value is passed.

## Example 1

```python
def fun(i, j=9):
    print(i, j)

fun(100, 200)
```

### Output

```text
100 200
```

👉 Default value `9` is overridden by `200`

---

## Example 2

```python
def fun(i, j=2):
    print(i, j)

fun(3)
```

### Output

```text
3 2
```

👉 `j` takes default value

---

## ❗ Rule (Important)

```python
# Non-default arguments must come before default arguments
```

Wrong example:

```python
# def fun(i=21, j):
#     print(i, j)
```

---

# 4️⃣ Mixing Positional and Keyword Arguments

## Example

```python
def fun(a, b, c):
    print(a, b, c)

fun(10, 20, 30)
fun(a=10, b=30, c=40)
fun(c=2, a=4, b=0)
fun(11, 12, c=13)
fun(3, b=5, c=8)
```

### Output

```text
10 20 30
10 30 40
4 0 2
11 12 13
3 5 8
```

---

## ❌ Wrong Usage

```python
# fun(10, b=2, c)
```

👉 This gives Syntax Error because positional arguments must come before keyword arguments.

---

# 5️⃣ Finding Largest Number Using Function

## Two Numbers

```python
def largest(a, b):
    if a > b:
        return a
    else:
        return b

print(largest(100, 200))
print(largest(20, 10))
```

### Output

```text
200
20
```

---

## Three Numbers (Using if-else)

```python
def largest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(largest(10, 20, 30))
print(largest(50, 20, 10))
```

### Output

```text
30
50
```

---

## Best Way (Using max function)

```python
def largest(a, b, c):
    return max(a, b, c)

print(largest(10, 20, 70))
```

### Output

```text
70
```

---

# 🚀 Key Concepts Summary

| Concept              | Meaning                    |
| -------------------- | -------------------------- |
| Positional Arguments | Based on position          |
| Keyword Arguments    | Based on parameter name    |
| Default Arguments    | Pre-defined values         |
| *args                | Multiple positional values |
| **kwargs             | Multiple keyword values    |
| return               | Sends value back           |
| max()                | Finds largest value        |

---

# 🧠 Quick Revision Rule

👉 Positional → order matters
👉 Keyword → name matters
👉 Default → fallback value
👉 max() → easiest way to find largest

---

# 🎯 Conclusion

Functions in Python become powerful when combined with different types of arguments. Understanding them helps write clean, flexible, and reusable code.
