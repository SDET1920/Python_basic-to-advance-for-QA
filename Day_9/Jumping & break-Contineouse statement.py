#Break--

#Example 1- print (1 to 10) and break at 5.

for i in range(1,10):
    if i == 5:              #Means used break to (break block) at 5
        break
    print(i)

print("Program exit at 5")

# Example 2-- Print (1 to 10) and continue code till 10.

for i in range(1,10):
    if i==5:
        continue         #Means the code is continue till 10, we are not breaking here.
    print(i)
print("Program continue till 10")


# Example 3---- Write code (1 to 10) and break/continue at 3,5,7.

for i in range(1,10):
    if i==3 or i==5 or i==7:
        continue
    print(i)
print("Program Exit")


# Example 4--- Print (3, to 7)

for i in range(3,7,2):
    print(i)
