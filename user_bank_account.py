class BankAccount:

    def __init__(self, int_rate, balance):        
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate 
            return self

account1 = BankAccount(0.02, 100)
account2 = BankAccount(0.03, 1500)

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def make_deposit(self):
        self.account.deposit(300)
        print(self.account.balance)
        return self

    def make_withdrawal(self):
        self.account.withdraw(1000)
        return self
        
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account.balance}")
        return self
        

annie = User("Annie Jung", "annie@gmail.com")

annie.make_deposit()


