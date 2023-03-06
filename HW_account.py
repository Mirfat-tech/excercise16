
class HW_Account:

    def __init__(self, amount):
        self.balance = amount

    def deposit(self, amount):
        self.balance += amount
        return f"You have deposited £{amount}"

    def get_balance(self):
        return self.balance


    def withdraw(self, amount):
      if amount >= self.balance:
          try:
             self.balance -= amount
             print (f" £{amount} was withdrawn from your account")
          except InsufficientFunds as err:
              print(err)
          finally:
              print(f"You have insufficient funds.")

# class Exceptions:
#           try:
#               if amount >= self.balance:
#               def withdraw(self, amount):
#
#
# #         # print (f" £{amount} was withdrawn from your account")
#           except withdraw as err:
#               print(err)
#               print(f"You have insufficient funds.")


# Raise keyword was used to intentionally create an error to
# make sure we get the input we’re looking for

    # def withdraw(self, amount):
    #     if amount >= self.balance:
    #         try:
    #             self.balance -= amount
    #         except withdraw as err:
    #             print(err)
    #             print(f"You have insufficient funds.")
