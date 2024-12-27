class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount, acctName): 
        # initialAmount: intial amount present
        # acctName: Name of account
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}', created.\n Balance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit complete.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nAccount '{self.name}' only has balance ${self.balance:.2f}"
                )
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.getBalance()

        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print('\n***********\n\nBeginning Transfer.. 🚀')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer complete!✅\n\n***********")
        
        except BalanceException as error:
            print(f"\nTransfer interrupted. ❌ {error}")

class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        # return super().deposit(amount)
        self.balance = self.balance + (amount * 1.05) # additional 5%
        print("\nDeposit complete.")
        self.getBalance()
            
class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5

    def withdraw(self, amount):
        # return super().withdraw(amount)
        try:
            self.viableTransaction(amount+self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw complete.")
            self.getBalance()

        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")



