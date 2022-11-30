class BANKACCOUNT:
    def __init__(self, int_rate=0, balance=0):
        self.interest = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("ERROR: Insufficent funds!")
        return self

    def display_account_info(self):
        print(
            f"Shants account balance is: ${self.balance}.")

    def yield_interest(self):
        if self.balance > 0:
            self.balance += round(self.balance*self.interest)
        else:
            print("No positive balance to calculate intrest toward.")
        return self


BoA = BANKACCOUNT(0.005, 1400)
WellsFargo = BANKACCOUNT(0.00067, 500)

BoA.deposit(1100).deposit(90).deposit(40).withdraw(
    500).yield_interest().display_account_info()

WellsFargo.deposit(1200).deposit(300).withdraw(200).withdraw(700).withdraw(
    40).withdraw(130).yield_interest().display_account_info()