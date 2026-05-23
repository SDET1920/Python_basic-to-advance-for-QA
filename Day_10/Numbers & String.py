#NUmbers..

num1= 100
num2= 200

print(type(num1))
print(type(num2))


# Find maximum value.

print(max(10,20,40,90,10))

# Find max number in between 1 to 100.

print(max(range(1, 101)))


# Convert int to float and Complex.
x = 5

print(float(x))    # int to float
print(complex(x))  # int to complex

# String----it's immutable

#Ways to create string variable:

s= "welcome"
s= 'welcome'
s= str("welcome")
s= str('welcome')

#Create empty string variable:

name= ""
name= ''
name= str()

#Note--- In string they assign a seperate memory to execute result.

str="wel"
print(id(str))  #here id will be print for result (2117327324048)


#Example (+) and (*) with string.  here (concatenation/joinging)

str= "welcome"
print(str + "Programing")

print(str*3)