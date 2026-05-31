# Python Dictionary Examples

## What is a Dictionary in Python?

A Dictionary in Python is used to store data in `key : value` pairs.

Dictionary is:

* Ordered
* Mutable
* Does not allow duplicate keys

---

# Creating a Dictionary

```python
mycar = {
    "brand": "Hyundai",
    "model": "Venue",
    "year": 2026,
    "price": 9
}

print(mycar)
```

### Output

```python
{'brand': 'Hyundai', 'model': 'Venue', 'year': 2026, 'price': 9}
```

---

# Accessing Values

## Using Key

```python
print(mycar["brand"])
```

### Output

```python
Hyundai
```

---

# Using `get()` Method

```python
print(mycar.get("model"))
```

### Output

```python
Venue
```

---

# Adding New Item

```python
mycar["color"] = "White"

print(mycar)
```

### Output

```python
{'brand': 'Hyundai', 'model': 'Venue', 'year': 2026, 'price': 9, 'color': 'White'}
```

---

# Updating Value

```python
mycar["price"] = 12

print(mycar)
```

### Output

```python
{'brand': 'Hyundai', 'model': 'Venue', 'year': 2026, 'price': 12}
```

---

# Removing Item

## Using `pop()`

```python
mycar.pop("year")

print(mycar)
```

### Output

```python
{'brand': 'Hyundai', 'model': 'Venue', 'price': 9}
```

---

# Removing Last Item

## Using `popitem()`

```python
mycar.popitem()

print(mycar)
```

---

# Deleting Dictionary

## Using `del`

```python
del mycar
```

After deletion:

```python
NameError
```

---

# Clearing Dictionary

## Using `clear()`

```python
mycar.clear()

print(mycar)
```

### Output

```python
{}
```

---

# Checking Key in Dictionary

```python
if "price" in mycar:
    print("Key exists")
else:
    print("Key not found")
```

---

# Checking Value in Dictionary

```python
if 9 in mycar.values():
    print("Value exists")
else:
    print("Value not found")
```

---

# Dictionary Methods

| Method     | Purpose                 |
| ---------- | ----------------------- |
| `keys()`   | Returns all keys        |
| `values()` | Returns all values      |
| `items()`  | Returns key-value pairs |
| `get()`    | Access value safely     |
| `update()` | Update dictionary       |
| `pop()`    | Remove specific item    |
| `clear()`  | Remove all items        |

---

# Loop Through Dictionary

## Print Keys

```python
for x in mycar:
    print(x)
```

---

## Print Values

```python
for x in mycar.values():
    print(x)
```

---

## Print Keys and Values

```python
for x, y in mycar.items():
    print(x, y)
```

---

# Nested Dictionary

```python
student = {
    "student1": {
        "name": "Shiv",
        "age": 25
    },
    "student2": {
        "name": "Rahul",
        "age": 24
    }
}

print(student)
```

---

# Important Interview Questions

| Question                          | Answer |
| --------------------------------- | ------ |
| Is dictionary ordered?            | Yes    |
| Are duplicate keys allowed?       | No     |
| Can values be duplicated?         | Yes    |
| Is dictionary mutable?            | Yes    |
| Does dictionary support indexing? | No     |

---

# Difference Between List, Tuple, Set, Dictionary

| Data Type  | Ordered | Mutable | Duplicate Allowed |
| ---------- | ------- | ------- | ----------------- |
| List       | Yes     | Yes     | Yes               |
| Tuple      | Yes     | No      | Yes               |
| Set        | No      | Yes     | No                |
| Dictionary | Yes     | Yes     | Keys No           |

---

# Conclusion

A dictionary is mainly used when data should be stored in:

* Key-value format
* Fast lookup operations
* Structured data representation
