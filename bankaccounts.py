#vars () = retrieves all properties from a class
##git add . = allows current working directory to work through git hub


class Account(object):
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdrawal(self, amount):
        if (self.balance < 0):
            self.balance = self.balance + amount
            print "Your withdrawal will cause an overdraft. Please try again."
        else:
            self.balance = self.balance - amount
            print "Please find your withdrawal for %s!" %(amount)
            print "Your account is now at %s." %(self.balance)
            print "Have a nice day, %s!" %(self.name)




John = Account("John", 500)
print John.name
print John.balance

John.withdrawal(100)


'''
John.deposit(1000)

print John.balance

John.withdrawal(50)

print John.balance

John.withdrawal(1500)

print John.balance
'''
