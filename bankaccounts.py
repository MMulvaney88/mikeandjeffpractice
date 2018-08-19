#vars () = retrieves all properties from a class
##git add . = allows current working directory to work through git hub


class Account(object):
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance

    def deposit(self, balance):
        self.balance = self.balance + balance

    def withdrawal(self, balance):
        self.balance = self.balance - balance

John = Account("John", 500)
print John.name
print John.balance

John.deposit(1000)

print John.balance

John.withdrawal(1500)

print John.balance
