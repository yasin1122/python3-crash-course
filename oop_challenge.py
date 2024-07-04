class Account:
    
    def __init__(self, owner, balance=0) -> None:
        self.owner = owner
        self.balance = balance

    def __str__(self) -> str:
        return (f"Account owner:   {self.owner}\n"
                f"Account balance: ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit Accepted")

    def withdraw(self, amount):
        # withdraws may not exceed available balance
        if amount <= self.balance and amount > 0:
            self.balance -= amount
            print("Withdrawal Accepted")
        else:
            print("Funds Unavailable!")

account1 = Account('Joe', 100)
print(account1)
print(account1.owner, account1.balance)
account1.deposit(50)
account1.withdraw(75)
account1.withdraw(500)