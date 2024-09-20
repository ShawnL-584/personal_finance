class Employee:
    def __init__(self):
        self.income = 0

    def earn_money(self, money):
        self.income += money
        self.__tax = self.income * 0.05

    def get_tax(self):
        return self.__tax

    @property
    def tax_amount(self):
        return self.income * 0.05

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        self.income = tax_amount * 20


shawn = Employee()
shawn.earn_money(100)
print(shawn.get_tax())

shawn.earn_money(200)
print(shawn.get_tax())

print(shawn.tax_amount)

shawn.tax_amount = 100
print(shawn.income)
