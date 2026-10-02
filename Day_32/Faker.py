# Faker-- it's a libray used to generate fake data for testing.


# Example 1-   Create a fake data like (Name, Email, Address, and phone number) for testing.


from faker import Faker

fake=Faker()

print(fake.name())
print(fake.email())
print(fake.address())
print(fake.phone_number())


# Example 2- Create a fake data in Indian format.

from faker import Faker

fake=Faker("en_IN")
print(fake.name())
print(fake.email())
print(fake.address())
print(fake.phone_number())


# Example 3- Create a fake data in Indian format for hindi.

from faker import Faker

fake=Faker("hi_IN")
print(fake.name())
print(fake.email())
print(fake.address())
print(fake.phone_number())