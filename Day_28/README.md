Python Encapsulation Examples

This repository contains simple Python examples demonstrating Encapsulation using classes and private attributes.

📌 Examples Included
1. Bank Account

The BankAccount class demonstrates how to manage a bank balance using methods such as:

deposit() — Adds money to the account.

get_balance() — Returns the current balance.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def get_balance(self):
        return self.balance


account = BankAccount(1000)
account.deposit(500)

print(account.get_balance())


Output:

1500

2. Mobile Phone

The Mobile class demonstrates the use of a private attribute using double underscores (__password).

The password cannot be accessed directly in the usual way. Instead, methods are used to change and display the password.

class Mobile:
    def __init__(self):
        self.__password = 1234

    def change_password(self, new_password):
        self.__password = new_password

    def show_password(self):
        return self.__password


phone = Mobile()
phone.change_password(5678)

print(phone.show_password())


Output:

5678

🧠 Concept: Encapsulation

Encapsulation is an important concept of Object-Oriented Programming (OOP).

It means keeping data and the methods that operate on that data together inside a class and controlling how the data can be accessed or modified.

In Python, a double underscore (__) is commonly used for name mangling, which helps restrict direct access to an attribute.

Example
class Mobile:
    def __init__(self):
        self.__password = 1234


Here, __password is treated as a private-style attribute.

📂 Project Structure
.
├── bank_account.py
├── mobile.py
└── README.md
