
## What is a Set in Python?

A Set in Python is an unordered collection of unique elements.

### Features of Set

* Duplicate values are not allowed
* Unordered collection
* Mutable (can add/remove items)
* Does not support indexing

---

# Creating a Set

```python
myset = {"QA", "Manual", "Automation"}
print(myset)
```

### Output

```python
{'QA', 'Manual', 'Automation'}
```

---

# Adding Element in Set

## Using `add()`

```python
myset = {"QA", "Manual"}

myset.add("Automation")

print(myset)
```

### Output

```python
{'QA', 'Manual', 'Automation'}
```

---

# Adding Multiple Elements

## Using `update()`

```python
myset = {"QA"}

myset.update(["Manual", "Automation"])

print(myset)
```

### Output

```python
{'QA', 'Manual', 'Automation'}
```

---

# Removing Element from Set

## Using `remove()`

```python
myset = {"QA", "Manual", "Automation"}

myset.remove("Manual")

print(myset)
```

### Output

```python
{'QA', 'Automation'}
```

---

# Union of Sets

```python
myset1 = {"QA", "Automation"}
myset2 = {"SDET", "Manual"}

result = myset1.union(myset2)

print(result)
```

### Output

```python
{'QA', 'Automation', 'SDET', 'Manual'}
```

---

# Clearing Set

## Using `clear()`

```python
myset = {"QA", "Manual"}

myset.clear()

print(myset)
```

### Output

```python
set()
```

---

# Deleting Set

## Using `del`

```python
myset = {"QA", "Manual"}

del myset
```

After deleting, accessing `myset` will give:

```python
NameError
```

---

# Important Interview Questions

| Question                               | Answer |
| -------------------------------------- | ------ |
| Does set allow duplicates?             | No     |
| Is set ordered?                        | No     |
| Does set support indexing?             | No     |
| Can we modify set?                     | Yes    |
| Can we update specific value directly? | No     |

---

# Difference Between `add()` and `update()`

| Method     | Purpose               |
| ---------- | --------------------- |
| `add()`    | Add single element    |
| `update()` | Add multiple elements |

---

# Common Mistake

```python
myset.update("SDET")
```

Output:

```python
{'S', 'D', 'E', 'T'}
```

### Reason

`update()` treats string as iterable and adds characters individually.

### Correct Way

```python
myset.add("SDET")
```

---

# Conclusion

Sets are useful when:

* Duplicate values should not be allowed
* Fast membership checking is required
* Order is not important
