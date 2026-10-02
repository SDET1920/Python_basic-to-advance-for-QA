# Example 1- Get the current date and time.

from datetime import datetime

now=datetime.now()

print(now)


# Example 2- Get only date.

from datetime import date

today=date.today()
print(today)

# Example 3- Get individual date and time component.

from datetime import datetime

now= datetime.now()

print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hours:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

# Example 4- Formated date and time.

from datetime import date

now=datetime.now()

formatted= now.strftime("%d-%m-%Y %H:%M:%S")

print(formatted)

