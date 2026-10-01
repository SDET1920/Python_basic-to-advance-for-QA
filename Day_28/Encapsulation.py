## Example 1 and Example 2 below.

## class BankAccount to check the balance and deposit..

class BankAccount:
    def __init__(self, balance):
        self.balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def get_balance(self):
        return self.balance


account = BankAccount(1000)
account.deposit(500)

print(account.get_balance())


## Example mobile phone to change the password.

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