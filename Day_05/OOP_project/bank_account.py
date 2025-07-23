class Balance_exception(Exception): 
    pass

class Bank_account:
    def __init__(self, initial_amount, account_name):
        self.balance = initial_amount
        self.account_name = account_name
        print(f"\nAccount {self.account_name}'s created.\nBalance: ${self.balance:.2f}")
    
    def get_balance(self): 
        print(f"\nAccount '{self.account_name}' balance = ${self.balance:.2f}. ")
    
    def deposit(self, amount): 
        self.balance += amount
        print("\nDeposit completed!")
        self.get_balance()
    
    def via_withdraw(self, amount): 
        if amount <= self.balance: 
            return
        else: 
            raise Balance_exception(f"'{self.account_name}' only has ${self.balance}!")
    
    def withdraw(self, amount): 
        try: 
            self.via_withdraw(amount)
            self.balance -= amount
            print("\nWithdraw completed")
            self.get_balance()
        except Balance_exception as error: 
            print(f"\nWithdraw interupted: {error}")
    
    def transfer(self, amount, account): 
        try: 
            self.via_withdraw(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("Transfer completed! ✅")
        except Balance_exception as error: 
            print(error)
            print("Transfer interupted!")

class SavingAccount(Bank_account): 
    def __init__(self, initial_amount, account_name):
        super().__init__(initial_amount, account_name)
        self.fee = 5 
    
    def withdraw(self, amount):
        try: 
            self.via_withdraw(amount + self.fee)
            self.balance -= amount + self.fee
            print("Withdraw completed!")
            self.get_balance()
        except Balance_exception as error: 
            print(error)
    
            