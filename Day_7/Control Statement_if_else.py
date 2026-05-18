# Write program to a person is eligible for vote or not.


# Step- a person is 18 year old then eligible.
# Step- a person is under 18 year then not eligible.

age=2

if age>=18:
    print("eligble for vote")
else:
    print("Not eligible for vote")  #Note eligibel bcz (10>=18) a person under 18.


## write program to find even or odd number.

num = 10

if num%2==0:
    print("it's even number")
else:
    print("it's ODD number")

#Example-  if-elif-else statement


marks = 90
if marks >= 85:
    print("you got Grade: A")
elif marks >= 65:
    print("you got Grade: B")
else:
    print("you got Grade: C")

#Example of weekdays (1 to 7).

week_day = 8

if week_day == 1:
    print("Today is Sunday")

elif week_day == 2:
    print("Today is Monday")
elif week_day == 3:
    print("Today is Tuesday")

elif week_day == 4:
    print("Today is wednesday")

elif week_day == 5:
    print("Today is Thursday")

elif week_day == 6:
    print("Today is Friday")
elif week_day == 7:
    print("Today is Saturday")

else:
    print("Invalid week days, we don't have that weekday in calender")


## Example of Month's.

month = 11
if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")

else:
    print("Invalid month number we don't have that month in calender")