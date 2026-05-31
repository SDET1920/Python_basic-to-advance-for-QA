## Dictionary is collection, which is unordered, changable (mutable), and index based on keys.

## it written in curly brackets {} and they have key:value system.

## Example--

#Key          value
#Product 1 :  100

## Create a dictionary---

mydic= {
    1:"x", 2:"y", 3:"z"
}

print(mydic)


## Access itme from hundai car details.

mycar= {
      "brand": "Hundai",
       "Modle": "venue",
       "year": 2026,
       "Price": 9
}

print(mycar)   ## we can print all values

print(mycar["brand"])    ## we can print specific value.
print(mycar['year'])      ## we can print specific value.

## Access values using get()

mycar= {
      "brand": "Hundai",
       "Modle": "venue",
       "year": 2026,
       "Price": 9
}

print(mycar.get("Price"))
## or

x= mycar.get(("Price"))
print(x)

## Change values in dictionary-----

mycar= {
      "brand": "Hundai",
       "Modle": "venue",
       "year": 2026,
       "Price": 9
}

mycar["brand"]= "TATA"

print(mycar)


## remove item to dictionary

mycar = {
    "brand": "Hundai",
    "Modle": "venue",
    "year": 2026,
    "Price": 9
}

mycar.pop("Price")      ## pop() will remove the specfic item from dictionary.
print(mycar)


## Read key/item in dictionary using loop...

mycar= {
      "brand": "Hundai",
       "Modle": "venue",
       "year": 2026,
       "Price": 9
}

for i in mycar:        ## Only key is print in output section..
    print(i)

for i in mycar:
    print(mycar[i])     ##Only Value is print in output section

## or other example to print key/item using loop..

for i in mycar.values():              ## Only values print
    print(i)

for i in mycar.keys():                  ## only keys print
    print(i)


for x,y in mycar.items():        ## here key and values both will be print in same time check in output section...
    print(x,y)



## Check key values is exit or not in dictionary..

mycar= {
      "brand": "Hundai",
       "Modle": "venue",
       "year": 2026,
       "Price": 9
}

if "Price" in mycar:
    print("Yes the Price:9 is present in values")
else:
    print("No the values is not present")

## Check values is exit or not in dictionary..

mycar = {
    "brand": "Hundai",
    "Modle": "venue",
    "year": 2026,
    "Price": 9
}

if 9 in mycar.values():           ## here .values() will be use for print values only.
    print("Yes value 9 is present")
else:
    print("No value is not present")

## Check length in dictionary
mycar = {
    "brand": "Hundai",
    "Modle": "venue",
    "year": 2026,
    "Price": 9
}

print(len(mycar))


## remove item to dictionary

mycar = {
    "brand": "Hundai",
    "Modle": "venue",
    "year": 2026,
    "Price": 9
}

mycar.pop("Price")
print(mycar)

## remove item to dictionary

mycar = {
    "brand": "Hundai",
    "Modle": "venue",
    "year": 2026,
    "Price": 9
}

mycar.pop("Price")      ## pop() will remove the specfic item from dictionary.
print(mycar)


## we need to delete single data using----  del function

mycar = {
    "brand": "Hundai",
    "Modle": "venue",
    "year": 2026,
    "Price": 9
}

del mycar["Price"]
print(mycar)


## if you want to delete full data.

mycar = {
    "brand": "Hundai",
    "Modle": "venue",
    "year": 2026,
    "Price": 9
}

# del mycar
# print(mycar)            #NameError: name 'mycar' is not defined


## Clear all data in dictionary..
mycar = {
    "brand": "Hundai",
    "Modle": "venue",
    "year": 2026,
    "Price": 9
}

mycar.clear()
print(mycar)             ## here the blank dictionary will be print only..


### Copy dictionary  with copy function----copy()

mycar = {
    "brand": "Hundai",
    "Modle": "venue",
    "year": 2026,
    "Price": 9
}

mycar1= mycar.copy()
print(mycar1)


## Copy dictionary  with out  copy function----
mycar = {
    "brand": "Hundai",
    "Modle": "venue",
    "year": 2026,
    "Price": 9
}

mycar1=mycar
print(mycar1)

## Nested Dictionary
student = {
    "student1": {
        "name": "Shiv",
        "age": 25
    },
    "student2": {
        "name": "Rahul",
        "age": 24
    }
}

print(student)