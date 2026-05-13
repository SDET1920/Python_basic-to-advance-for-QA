## Delete the variable in code

a=10
b=20
print(a,b)
print(a)
print(b)


## if you want to delete 'C' vairable in code.
c=10
del c

## Exception using for message (without exception it's not possible)
try:
    print(c)
except NameError:
    print("Variable 'c' has been deleted.")