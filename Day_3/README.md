## We write a program, where print a and b values for print variable only. 

1- Then we have to decide to delete "c" variable from code.

2- while deleting the "c" variable there will be 'c' error in Run window (Name Error: name 'c' is not defined)

3- because the 'c' variable has been deleted so the error msg occuring (Name Error: name 'c' is not defined)



#if you want to delete 'C' vairable in code.

c=10
del c

#Exception using for message (without exception it's not possible)

try:
    print(c)
except NameError:
    print("Variable 'c' has been deleted.")