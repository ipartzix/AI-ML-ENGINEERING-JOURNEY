class Phone:
    def __init__(self, price, brand, model):
        self.price = price
        self.brand = brand
        self.model = model

    def buy(self):
        print("buy a phone")


# child class can not use or access parent class hidden member can not access

class SmartPhone(Phone):
    def buy(self):
        print("buy a smart phone ")
        pass


s = SmartPhone(100000, "apple", "18 PRO MAX")
# print(s)
s.buy()  # when 2 or more method are available in parent and child both class it always run child class method  it called method overwriting
print("it is method overriding polymorphism")
