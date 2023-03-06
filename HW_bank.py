
from HW_account import HW_Account

class Current(HW_Account):
    def __init__(self, amount):
        super().__init__(self)
        self.balance = amount

# The super() function is used to give access to methods and properties of a parent or sibling class.
# The super() function  returns an object that represents the parent class

    def __str__(self):
        return f"Eyasmin has £{eyasmin_c.get_balance()} in her current account and £{eyasmin_s.get_balance()} in her savings"


class Savings(HW_Account):
    def __init__(self, amount):
        super().__init__(self)
        self.balance = amount

eyasmin_c = Current(1000)
eyasmin_s = Savings (200)


pam_c = Current(500)
pam_s = Savings(100)
# print(f"Pam has £{pam_c.get_balance()} in her current account and £{pam_s.get_balance()} in her savings")
#
# pam_s.deposit(150)
# print(f" Pam now has £{pam_s.get_balance()} extra in her account")


eyasmin_c.withdraw(2000)
print(f"Eyasmin balance: £{eyasmin_c.get_balance()}")
