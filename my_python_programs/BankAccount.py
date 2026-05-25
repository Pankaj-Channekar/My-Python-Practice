class BankAccount:

    def __init__(self,bank_name,bal):
        self.bank_name=bank_name
        self.bal=bal
    
    def check_balance(self):
        print(f"Balance is : {self.bal}")
        
    def deposit(self,amount):
        self.amount=amount
        self.bal +=self.amount
    
    def withdraw(self,amount):
        self.amount=amount
        try:
            if self.bal < self.amount:
                raise Exception ("Insufficient Balance")
                   
        except Exception:
            print("Your Balance is not enough for withdrawl")
        
        else:
            self.bal -=self.amount
            
    
bank1 = BankAccount("Axis", 15000)
print("Initially :-- ")
bank1.check_balance()
bank1.deposit(1000)
print("After deposit :-- ")
bank1.check_balance()
bank1.withdraw(22000)
print("After withdraw :-- ")
bank1.check_balance()

        
        
