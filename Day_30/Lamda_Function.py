# Lamda function- it's small fucntion to use when need a short function temporarily.

# Syntax-   lamda argument: expression

# it's specially use with sorted(), map(), filter() function.


# Example 1-   square of any value.

square= lambda x: x*x

print(5)

# Example 2-  Multiple arguments.

add= lambda a,b: a + b

print(add(5,20))


# Example 3-  Sorted()-- to sort value--

student= [
    ("Alicia", 85),
    ("Bob", 72),
    ("Charlie", 91)
]

student.sort(key= lambda student: student[1])
print(student)


# Example 4- filter()--- for condtion and filter the values.

numbers= [1,2,3,4,5,6,7,8]

even= list(filter(lambda x: x%2==0, numbers))
print(even)

# Example 5- map()-- The same lambda function apply the same operation to every item.

# Double every number

numbers=[1,2,3,4,5,6]

result=list(map(lambda x: x*2, numbers))

print(result)
