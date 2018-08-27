#vars () = retrieves all properties from a class
##git add . = allows current working directory to work through git hub


class Account(object):
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        #The DEPOSIT is added to the balance. Message is given on new amount
        self.balance = self.balance + amount
        print "$%s has been added to your account." %(amount)
        print "Your new balance is $%s." %(self.balance)
        print "Have a nice day, %s" %(self.name)

    def withdrawal(self, amount):
        #The WITHDRAWL is deducted from balance. Message is given on new amount
        #If account is left <0, withdrawal is cancelled.
        self.balance = self.balance - amount
        if (self.balance < 0):
            self.balance = self.balance + amount
            print "Your withdrawal will cause an overdraft. Please try again."
            print "Your balance is currently at %s." %(self.balance)
        else:
            print "Please find your withdrawal for $%s!" %(amount)
            print "Your account is now at $%s." %(self.balance)
            print "Have a nice day, %s!" %(self.name)

    #Transfer function - To Be Completed
    #def transfer(self, amount, newAccount):
        #select primary Account
        #WITHDRAW $$$ from primary Account
        #DEPOSIT $$$ into newAccount

'''
#Testing the DEPOSIT function
Jeff = Account("Jeff Carroll", 2000)
Jeff.deposit(1000)
'''
'''
#Testing the WITHDRAWAL function
John = Account("John", 500)
John.withdrawal(100)
'''
