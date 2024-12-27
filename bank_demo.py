from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.getBalance()
Dave.deposit(50)
Dave.withdraw(50000)
Dave.withdraw(500)

Dave.transfer(10000, Sara)
Dave.transfer(100, Sara)

Jim = InterestRewardsAcct(1000, "Jim")
Jim.getBalance()
Jim.deposit(100)
Jim.transfer(50, Dave)

Blaze = SavingsAcct(9000, "Blaze")
Blaze.getBalance()
Blaze.deposit(50)
Blaze.transfer(90000, Dave)
Blaze.transfer(900, Sara)
