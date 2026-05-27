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

## Slicing operator []

str= "welcome"

print(str[1:3])

print((str[:6]))   #here starting index is (0), whether you have define or not. it by default (0).

print(str[2:])   #it will start form 2 till the end will be print.

print(str[1:-1])   # here start from 1 (e), but -1 wil caluclate from last so (-1 means (e)).

print(str[1:-2])   # here start from 1 (e), but will be end at (-2) (m)


## ord () and chr()

print(ord("A"))        #ord() will be return the ASCII code.

print(chr(65))        #chr() will be return character represented by ASCII number.



## Exaple max(), min(), len()

print(max("ABC"))

print(max("DCABTECH"))

print(min("abc"))

print(min("ABC"))

print(min("BcDefG"))

print(len("abc"))

print(len('Shivam'))

# Example in() and not-in() Operator.

s = "Shivam"

print("Shiv" in s)

print("rahul" in s)

print("Shiv" not in s)

print("rahul" not in s)

# String Compression

print("shiv" == "shiv")

print("shiv" == "radha")

print("shiv" != "shivam")

print('arrow' > 'arro')

print("right" >= "left")  #right bigger then left bcz as per character wise.

print("teech" < "tee")

print('yellow' <= 'fellow')   #yellow is bigger then fellow as per string number wise.

print("abc" > '')   #here "abc" is bigger then space.

# Example testing string true or false.

s= "welcome"

print(s.isalpha())    #welcome is alphabate.

print(s.isalnum())  #  it will not print bcz "welcome" is string value.

print("welcome".isalpha())

print("2012".isdigit())

print("Welcome to python".islower())

print("welcome to python".islower())

print("WELOCOME".isupper())


## Example serching for substring..

s= "welocome to python"
print(s.endswith("thon"))

print(s.endswith("shiv"))

print(s.startswith("wel"))

print(s.find("to"))    #Welcome to python (it provide a index value from (0) and if space it will also calculate)

print(s.count("t"))



## Example converting string

s="welcome to python"
s1=s.capitalize()
print(s1)         #capitalize (String to python") so only first letter will be capital.

s2=s.title()
print(s2)            #(all first letter will be convert into upper case (String To Python)

s3=s.lower()         #(all first letter will be small (string to python)
print(s3)

s4=s.upper()
print(s4)         ## The string will be convert into upper case.

s5=s.swapcase()
print(s5)         #in swapcase()--- it will convert lower to upper, or upper to lower.

s6=s.replace("to", "TO")


## Example 1  reverse string with slicing shortest method.

s="welocme"

rev_str= s[: : -1]          #"welcome" have 7 indexing  (staring "0", end "7", -1 will return every execution code)

print(rev_str)

## Example 2--reverse string with for loop.

s="welcome"

re_str=""

for i in s:
    re_str=i+re_str
print(re_str)


## Example 3-- Using reversed() Function
s = "welcome"

rev ="".join(reversed(s))

print(rev)


## Example 4- Using while loop


s = "welcome"

i = len(s) - 1

rev = ""

while i >= 0:
    rev = rev + s[i]
    i = i - 1

print(rev)


## Example--5   reverse string  Using Recursion
def reverse_string(s):

    if len(s) == 0:
        return s

    return reverse_string(s[1:]) + s[0]

print(reverse_string("welcome"))