#Numbers--

In Python, numbers are data types used to store numeric values. The main numeric types are:

1. Integer (int)

Output- <class 'int'>

2. Float (float)

Output-<class 'float'>

3. Complex (complex)- Numbers with a real and imaginary part.

Output- <class 'complex'>

# String-- String is immutable.

#Mutable-- Can change the value of the variable.

#Immutable-- Can not change the value of variable. 

#Ways to create string variable:

s= "welcome"
s= 'welcome'
s= str("welcome")
s= str('welcome')

#Create empty string variable:

name= ""
name= ''
name= str()


# Python String and Number Examples

This repository contains basic Python examples for:
- Numbers
- Type conversion
- String operations
- String slicing
- ASCII conversion
- String methods
- Searching substrings
- Case conversion

---

# Numbers Example

```python
num1 = 100
num2 = 200

print(type(num1))
print(type(num2))
```

### Output
```python
<class 'int'>
<class 'int'>
```

---

# Find Maximum Value

```python
print(max(10,20,40,90,10))
```

### Output
```python
90
```

---

# Find Maximum Number Between 1 to 100

```python
print(max(range(1,101)))
```

### Output
```python
100
```

---

# Type Conversion

```python
x = 5

print(float(x))
print(complex(x))
```

### Output
```python
5.0
(5+0j)
```

---

# String Creation

```python
s = "welcome"
s = 'welcome'
s = str("welcome")
s = str('welcome')
```

---

# Empty String Creation

```python
name = ""
name = ''
name = str()
```

---

# String Memory Allocation

```python
str = "wel"

print(id(str))
```

### Note
`id()` returns memory address of object.

---

# String Concatenation and Repetition

```python
str = "welcome"

print(str + "Programing")

print(str * 3)
```

### Output
```python
welcomePrograming
welcomewelcomewelcome
```

---

# String Slicing

```python
str = "welcome"

print(str[1:3])

print(str[:6])

print(str[2:])

print(str[1:-1])

print(str[1:-2])
```

### Output
```python
el
welcom
lcome
elcom
elco
```

---

# ord() and chr()

```python
print(ord("A"))

print(chr(65))
```

### Output
```python
65
A
```

---

# max(), min(), len()

```python
print(max("ABC"))

print(max("DCABTECH"))

print(min("abc"))

print(min("ABC"))

print(min("BcDefG"))

print(len("abc"))

print(len("Shivam"))
```

---

# in and not-in Operator

```python
s = "Shivam"

print("Shiv" in s)

print("rahul" in s)

print("Shiv" not in s)

print("rahul" not in s)
```

### Output
```python
True
False
False
True
```

---

# String Comparison

```python
print("shiv" == "shiv")

print("shiv" == "radha")

print("shiv" != "shivam")

print('arrow' > 'arro')

print("right" >= "left")

print("teech" < "tee")

print('yellow' <= 'fellow')

print("abc" > '')
```

---

# String Validation Methods

```python
s = "welcome"

print(s.isalpha())

print(s.isalnum())

print("welcome".isalpha())

print("2012".isdigit())

print("Welcome to python".islower())

print("welcome to python".islower())

print("WELOCOME".isupper())
```

---

# Searching for Substrings

```python
s = "welocome to python"

print(s.endswith("thon"))

print(s.endswith("shiv"))

print(s.startswith("wel"))

print(s.find("to"))

print(s.count("t"))
```

### Output
```python
True
False
True
9
2
```

---

# String Case Conversion

```python
s = "welcome to python"

s1 = s.capitalize()
print(s1)

s2 = s.title()
print(s2)

s3 = s.lower()
print(s3)

s4 = s.upper()
print(s4)

s5 = s.swapcase()
print(s5)

s6 = s.replace("to", "TO")
print(s6)
```

### Output
```python
Welcome to python
Welcome To Python
welcome to python
WELCOME TO PYTHON
WELCOME TO PYTHON
welcome TO python
```

---

# Important String Methods Summary

| Method | Description |
|--------|-------------|
| isalpha() | Checks alphabets only |
| isdigit() | Checks digits only |
| isalnum() | Checks alphabets and numbers |
| lower() | Converts to lowercase |
| upper() | Converts to uppercase |
| title() | Capitalizes each word |
| capitalize() | Capitalizes first letter |
| swapcase() | Changes upper to lower and lower to upper |
| replace() | Replaces substring |
| find() | Finds substring index |
| count() | Counts occurrences |

---

# Conclusion

These examples cover:
- Python numbers
- String operations
- String methods
- String slicing
- String searching
- Case conversion methods

## Reverse string example

- Slicing method
- for loop
- reversed() Function
- while loop
- Recursion