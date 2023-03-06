
class Person:
    def __int__(self, name, company):
        self.name = name
        self.company = company

# create class for Person
# defining int function contributes to creating the object
#  assigning the attributes to the method, that i will want to call later in employer
#  and customer

    # def __str__(self):
    #     print(f" I am {self.name} and I'm currently at {self.company} headquarters.")

class Employer(Person):
    def speak(self):
        return f"I'm selling the product to the customer"

class Customer(Person):
    def speak(self):
        return f"I'm buying the product from the customer"

#
# p = Person("Kia", "Apple")
# p.show()

c = Customer("Liam", "Amazon")
print(Person)












