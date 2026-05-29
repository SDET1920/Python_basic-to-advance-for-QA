## Collection-- it 4 type, list,tuple,set dicstionary.

mylist11= [10,20,30,40]
print(mylist11)

mylist2= ["apple", "banana", "SDET"]
print(mylist2)


mylist3= [1,2,3,4,"abc", 'def',17,9]
print(mylist3)

mylist4= list()
print(mylist4)   #it will contains empty list []


## Range of Indexing exmple---
## how accessing item from the list with single index value..
mylist11= [10,20,30,40]     #index alwasy start from (0).
print(mylist11[3])


mylist3= [1,2,3,4,"abc", 'def',17,9]
print(mylist3[5])

##  Method 1: Using multiple indexes
mylist3= [1,2,3,4,"abc", 'def',17,9]

print(mylist3[3], mylist3[5])




## Method 2: Store in variables then print.

mylist3= [1,2,3,4,"abc", 'def',17,9]

a=mylist3[4]
b=mylist3[5]

print(a)
print(b)


## Method 3: Using slicing
mylist3= [1,2,3,4,"abc", 'def',17,9]

print(mylist3[4:6])    #here logic of slicing [4:6] (4 is starting index so it will print, 6 is end index so one index will be less from 6


## last index will be print using (-index)

mylist5= [1,2,3,4,"abc", 'def',17,9]

print(mylist5[-1])
print(mylist5[-4])


## Change item value using index number

mylist=["apple", 'banana', 'cherry']
print(mylist)

mylist[0]= "SDET"
print(mylist)


## Read the list item using "for" loop...

mylist=["apple", 'banana', 'cherry']

for i in mylist:
    print(i)

## Read the list item using "while" loop...


mylist=["QA", 'QA_Automation', 'SDET', "SDET2", "SDET3"]

i = 0

while i <len(mylist):
    print(mylist[i])
    i=i+1
print("Successfully completed untill the conditioan match")


