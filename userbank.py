class BankAccount:
    def __init__(self, int_rate = 0.45, balance = 0):
        self.rate = int_rate
        self.account_balance = balance

    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self, amount):
        if self.account_balance - amount > 0:
            self.account_balance -= amount
        else:
            print("Low Balance  $3")
            self.account_balance -= 3
        return self

    def display_account_info(self):
        print("Balance", self.account_balance)
        return self




        #my brain hurts currently i am skipping the bonus parts 
        #i hope those are optional xD