## Set--- Set it collection and mutable, which is unorder and unidexed.

## Set written in {} curly brackets..



## Create Set

myset= {"QA", "manual QA", "Automation", 'SDET', 'SDET2'}

print(myset)


## Reading item/accessing item from set using for loop..

myset= {"QA", "manual QA", "Automation", 'SDET', 'SDET2'}

for i in myset:
    print(i)

## Value exist in set or not.

myset= {"QA", "manual QA", "Automation", 'SDET', 'SDET2'}

if "QA" in myset:
    print("Yes 'QA' is available in myset")
else:
    print(("No 'QA' is not available in myset"))


## Added itme in set..

myset= {"QA", "manual QA", "Automation", 'SDET', 'SDET2'}

myset.add("QAE")

print(myset)

## Added digit/interger value in set..

myset= {"QA", "manual QA", "Automation", 'SDET', 'SDET2'}

myset.add(1)

print(myset)


## Update multi values in set..

myset= {"QA", "manual QA", "Automation", 'SDET', 'SDET2'}

myset.update(["SDET3", 10])

print(myset)

## Find the number of item in set using len() function..

myset= {"QA", "manual QA", "Automation", 'SDET', 'SDET2'}

print(len(myset))


## Remove item from set or descard item from set.

myset= {"QA", "manual QA", "Automation", 'SDET', 'SDET2'}

myset.remove("QA")

print(myset)


## let suppose we want to remove a value which is not available in set values.
# myset= {"QA", "manual QA", "Automation", 'SDET', 'SDET2'}
#
# myset.remove("QAE")
#
# print(myset)                  ## KeyErrors--- 'QAE' because value is not available in set values.

## discard () function will use to remove value

myset= {"QA", "manual QA", "Automation", 'SDET', 'SDET2'}

myset.discard("manual QA")

print(myset)

## Clear values in one time...

myset= {"QA", "manual QA", "Automation", 'SDET', 'SDET2'}

myset.clear()

print(myset)


## Remove all values in set.

# myset= {"QA", "manual QA", "Automation", 'SDET', 'SDET2'}
#
# del myset                        #The variable myset is completely deleted from memory.
# print(myset)


## Join two set values using------union()
myset= {"QA", "manual QA", "Automation", 'SDET', 'SDET2'}

myset1= {1, 2}

myset2= myset.union(myset1)
print(myset2)

## Join two set values using------union operator |

myset= {"QA", "Automation", 'SDET', 'SDET2'}

myset1= {1, 2, 3}

myset2= myset | myset1
print(myset2)


## just update values in set values using update()

myset= {"QA", "Automation", 'SDET', 'SDET2'}


myset.update(["SDET1", 1])

print(myset)


## How to change a value in set?  using add()

# Step_1     Remove old value
# Step_2     Add new value


myset = {"QA", "Manual", "Automation"}

myset.remove("Manual")
myset.add("SDET")
print(myset)