#Concatenation-- it means joining, if both data type same then we can do concatenation.

a=10
b=20
print(a+b)


a=5
b="welcome"

#print(a+b)   #TypeError: unsupported operand

print(str(a) + "welcome")  #here we convert 5 into string now we can add integer+string value.

#Example 1- using (+) operator.

a= "hello"
b= "world"

c= a + "" + b
print(c)


# Example 2- with variable

first_name= "shiv"
second_name= "kishor"

full_name= first_name + " " +second_name  #(if space "" in commas then in full name will space or else it will add same)

print(full_name)

# Example 3- Using f-string (Best Method)

name= "shiv"
age = 25

print(f"name {name} and age is {age}")

#Example 4- Concatenation for lists

list1= [1,2]
list2= [3,4]

print(list1 + list2)

#Example 5- To create file path.

folder= "Documents"
file= "text.txt"

path= folder + "/" + file
print(path)

