# single user bank account
# make an instance of an account
# then implement different featues -> deposit, withdraw, get balance


class Bank_Account:
    def __init__(self, balance):
        self.balance = balance
        self.transactions = []
        
    
    def deposit(self, amount):
        if amount <=0:
            return "Invalid amount, please enter a amount greater than 0"
        else:
            self.balance += amount
            self.transactions.append(("Deposit", amount))
            return f"Deposit of ${amount} added successfully. New balance is: ${self.balance}"
        
    def withdaw(self, amount):
        if amount > self.balance:
            return f"Insufficient funds"
       
        self.balance -= amount
        self.transactions.append(("Withdraw", amount))
        return f"Withdraw of ${amount} complete. New balance is: ${self.balance}"
        
    
    
    def get_balance(self):
        return f"Balane amount: ${self.balance}"
    
    def transaction_history(self):
        return list(self.transactions)
        
    
    
account = Bank_Account(500)

print(account.deposit(1000))
print(account.withdaw(50))
print(account.get_balance())
print(account.transaction_history())
