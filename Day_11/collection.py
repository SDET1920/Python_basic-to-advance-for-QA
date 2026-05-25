# Python Collections Examples

# List: ordered, mutable, allows duplicate values
fruits = ["apple", "banana", "cherry", "apple"]
print("List:", fruits)
print("First item:", fruits[0])
fruits.append("orange")
print("After append:", fruits)
fruits.remove("banana")
print("After remove:", fruits)
print("Count of apple:", fruits.count("apple"))
print()

# Tuple: ordered, immutable, allows duplicate values
coordinates = (10, 20)
print("Tuple:", coordinates)
print("X coordinate:", coordinates[0])
# coordinates[0] = 5  # This would raise an error because tuples are immutable
print()

# Set: unordered, mutable, no duplicate values
unique_numbers = {1, 2, 3, 3, 4}
print("Set:", unique_numbers)
unique_numbers.add(5)
print("After add:", unique_numbers)
unique_numbers.discard(2)
print("After discard:", unique_numbers)
print()

# Dictionary: key-value pairs, keys are unique
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print("Dictionary:", person)
print("Name:", person["name"])
person["age"] = 26
person["job"] = "QA Engineer"
print("Updated dictionary:", person)
print()

# Using the collections module for useful collection types
from collections import Counter, defaultdict, namedtuple

# Counter: counts the number of occurrences in an iterable
sentence = "python collections are useful for QA automation"
word_counts = Counter(sentence.split())
print("Counter:", word_counts)
print("Most common word:", word_counts.most_common(1))
print()

# defaultdict: provides a default value for missing keys
scores = defaultdict(int)
scores["math"] += 90
scores["science"] += 85
print("defaultdict:", dict(scores))
print()

# namedtuple: lightweight object type with named fields
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 7)
print("namedtuple Point:", p)
print("Point x:", p.x)
print("Point y:", p.y)
