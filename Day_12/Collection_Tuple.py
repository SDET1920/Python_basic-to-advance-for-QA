## Tuple ()-- Tuple is immutable, which is in order and unchangeble.

# we can't change any thing and can't add, no changes is possible in tuple.

## Add, remove, update are not possible in tupe.. if add itme in tuple will get (Type error), if remove will get (Name error)

## we have possibility only once "tuple to list and list to tuple" then it's possible.

## creating tuple
mytuple= ("QA", "QA_automation","SDET")
print(mytuple)


## print tuple value using index value
mytuple= ("QA", "QA_automation","SDET")

print(mytuple[1])


## print tuple using range value with index..

mytuple= ("QA", "QA_automation","SDET", "SDET2", 'SDET3')

print(mytuple[1:4])

## Count tuple length

mytuple= ("QA", "QA_automation","SDET", "SDET2", 'SDET3')


print(len(mytuple))

## Copy tuple

mytuple= ("QA", "QA_automation","SDET", "SDET2", 'SDET3')

mytuple1= mytuple

print(mytuple1)

## join/combine tuple

mytuple= ("QA", "QA_automation","SDET", "SDET2", 'SDET3')

mytuple1= ("Manual tester", 1)

mytuple2= mytuple+mytuple1
print(mytuple2)


## Matching tupe using if/else

mytuple= ("QA", "QA_automation","SDET", "SDET2", 'SDET3')

mytuple1= ("Manual tester", 1)

if mytuple == mytuple1:
    print("Tuple is matching")
else:
    print("Tuple is not matching")


## Reading tupe itme using for loop

mytuple= ("QA", "QA_automation","SDET", "SDET2", 'SDET3')

for i in mytuple:
    print(i)




## changes in tuple using (Tuple to list to tuple)
#Step 1---Type to mylist
mytuple= ("QA", "QA_automation","SDET", "SDET2", 'SDET3')

mylist=list(mytuple)                     ## Tuple to list  and verified (Done)
print(mylist)

## Step 2-- chnages using index

mylist[0]= "Manual tester"              ## Changes done on index[0]="Manual tester"
print(mylist)

## Step 3--- change list to tuple

mytuple=tuple(mylist)              ## list to tuple

print(mytuple)                         ## Print mytuple...


## Repeat Tuple
mytuple = ("QA", "SDET")

print(mytuple * 2)                   ## ('QA', 'SDET', 'QA', 'SDET')


## Read Tuple Using   While Loop
mytuple = ("QA", "SDET", "Automation")

i = 0

while i < len(mytuple):
    print(mytuple[i])
    i = i + 1