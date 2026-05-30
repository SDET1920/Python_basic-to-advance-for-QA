**Tuple in Python**.

# Python Tuple

# Introduction

In Python, **Tuple** is one of the collection data types.

Collection types in Python:

1. List
2. Tuple
3. Set
4. Dictionary

A **Tuple** is:

* Ordered
* Allows duplicate values
* Immutable (cannot change values)
* Written using parentheses `()`

Example:

```python id="ayr4zj"
mytuple = ("QA", "SDET", "Automation")
```

---

# Create Tuple

```python id="vskj7y"
mytuple = ("apple", "banana", "cherry")

print(mytuple)
```

### Output

```python id="93ll4y"
('apple', 'banana', 'cherry')
```

---

# Tuple with Different Data Types

```python id="lmepxq"
mytuple = (10, 20, "QA", "SDET", True)

print(mytuple)
```

### Explanation

Tuple can store:

* Integer
* String
* Boolean
* Mixed data types

---

# Empty Tuple

```python id="c8klkr"
mytuple = ()

print(mytuple)
```

### Output

```python id="w55yye"
()
```

---

# Tuple Indexing

Index always starts from `0`.

```python id="z8dk0z"
mytuple = ("apple", "banana", "cherry")

print(mytuple[1])
```

### Output

```python id="yx86p1"
banana
```

---

# Negative Indexing

Negative index starts from the last element.

```python id="t8q54n"
mytuple = ("apple", "banana", "cherry")

print(mytuple[-1])
```

### Output

```python id="c4gkpw"
cherry
```

---

# Tuple Slicing

```python id="scl42g"
mytuple = ("QA", "Manual", "Automation", "SDET", "Tester")

print(mytuple[1:4])
```

### Output

```python id="h5hsh8"
('Manual', 'Automation', 'SDET')
```

### Slicing Logic

* Start index included
* End index excluded

---

# Read Tuple Using For Loop

```python id="7bjlwm"
mytuple = ("QA", "SDET", "Automation")

for i in mytuple:
    print(i)
```

### Explanation

Loop reads items one by one.

---

# Read Tuple Using While Loop

```python id="f6y4q7"
mytuple = ("QA", "SDET", "Automation")

i = 0

while i < len(mytuple):
    print(mytuple[i])
    i = i + 1
```

### Explanation

* `len()` returns tuple length
* Loop runs until condition becomes false

---

# Check Item Exists in Tuple

```python id="yz9vr4"
mytuple = ("QA", "SDET", "Automation")

if "QA" in mytuple:
    print("QA is available")
else:
    print("QA is not available")
```

---

# Length of Tuple

```python id="mfyt3t"
mytuple = ("QA", "SDET", "Automation")

print(len(mytuple))
```

### Output

```python id="4qjsuv"
3
```

---

# Tuple is Immutable

Tuple values cannot be changed.

```python id="s4a6kq"
mytuple = ("apple", "banana", "cherry")

mytuple[0] = "orange"
```

### Output

```python id="rbyn4o"
TypeError: 'tuple' object does not support item assignment
```

### Explanation

* Tuple does not allow modification after creation

---

# Convert Tuple to List

```python id="f8k2j7"
mytuple = ("apple", "banana", "cherry")

mylist = list(mytuple)

print(mylist)
```

### Explanation

Tuple can be converted into list for modification.

---

# Join Two Tuples

```python id="x8j3u1"
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2

print(tuple3)
```

### Output

```python id="n92lmt"
('a', 'b', 'c', 1, 2, 3)
```

---

# Repeat Tuple

```python id="d5r2me"
mytuple = ("QA", "SDET")

print(mytuple * 2)
```

### Output

```python id="dhjlwm"
('QA', 'SDET', 'QA', 'SDET')
```

---

# Count Values in Tuple

```python id="4tdk0n"
mytuple = (1, 2, 3, 1, 1, 4)

print(mytuple.count(1))
```

### Output

```python id="r6wsru"
3
```

### Explanation

* `count()` returns how many times value appears

---

# Find Index of Value

```python id="x5omrt"
mytuple = ("QA", "SDET", "Automation")

print(mytuple.index("SDET"))
```

### Output

```python id="52ccmn"
1
```

### Explanation

* `index()` returns position of value

---

# Difference Between List and Tuple

| List              | Tuple                |
| ----------------- | -------------------- |
| Mutable           | Immutable            |
| Uses `[]`         | Uses `()`            |
| Can modify values | Cannot modify values |
| Slower            | Faster               |

---

# Conclusion

In this Tuple tutorial, we learned:

* Tuple creation
* Indexing
* Slicing
* Loops
* Length checking
* Tuple methods
* Joining tuples
* Immutable behavior

Tuple is useful when data should not be changed after creation.
