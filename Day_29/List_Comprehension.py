#List comprehension- is a short and simple way to create a new list from an existing iterable such as a list, range, or string.

#Basic Syntax-------   new_list = [expression for item in iterable]



#Example 1--- create square using list comprehension approch.

squares= [i*i for i in range (1,6)]

print(squares)


## Example 2-  Print even numbers from 1 to 11 with condition.

even= [i for i in range(1,11) if i%2==0]

print(even)

## Example 3- if-else for even and odd number in list comprehension.

result= ["Even" if i%2==0 else "Odd" for i in range(1,20)]

print(result)

## Example 4- if-else for even and odd number in list comprehension (only enen and odd number will find out and print)

numbers = range(1,20)

even = [i for i in numbers if i%2==0]
odd= [i for i in numbers if i%2!= 0]

print(even)
print(odd)