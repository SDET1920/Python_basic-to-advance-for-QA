## Loops

#range(10)     (0--10)

#range(1,10)   (1---9)

#range(1,10,2)   (1 is starting time, 10 end point, 2 is incrementation)


#Example 1 (values between the range)

print(range(10))

# Example 2 (values between the range with list)

print(list(range(10)))      #list()- function found the value in between range.

# Example 3-- only odd number between (1 to 10).

print(list(range(1,10,2)))     #(1 starting, 10 end point, 2 is incremnetal)

# Example 4-- Only even number between (1 to 10)

print(list(range(2,10,2)))     #(0 starting, 10 end point, 2 is incremnetal)


## Example 5--  print decending order from (10 to 1)

print(list(range(10,1,-1)))        #(10 starting, 1 end point, -1 is incremnetal)

## Example 6-- Print (-10 to -5) values in decending order.

print(list(range(-10,-5,1)))


## For loop example-- Ex- list, type, string.

# Example 1--print (0 to 10) num using for loop.

for i in range(10):
    print(i)

# Example 2-- Print (1 to 11) num using for loop.

for i in range(1,11):
    print(i)

## Example 3- Print (-11, to -5) num using for loop.

for i in range(-10,-5):
    print(i)

## Example 4- Print only even number from (1 to 20).

for i in range (0,20,2):
    print(i)


# Example 5-- Print only Odd number from (1 to 20).

for i in (range(1,20,2)):
    print(i)

## Example 6-- Print only Odd number from (1 to 20) with list().

number= list(range(1,20,2))
print(number)

## Example 7- print in decdenting order (10 to 1).

for i in range(10,0,-1):
    print(i)


# While loop-- initialize condition in incremnet/decrement and executed multiple times till the condition become false.

# Example 1----write program to print (1 to 10) usin while loop.

i=1
while i<=10:
    print(i)
    i=i+1
print("Done!")

# Example 2----- Write program to print decending order number (10 to 1)

i=10
while i>=1:
    print(i)
    #i=i-1
print("Completed in decending order from 10 to 1")