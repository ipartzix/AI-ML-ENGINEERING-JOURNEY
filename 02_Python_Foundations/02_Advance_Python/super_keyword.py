class Phone:
    def __init__(self, price, brand, camera):
        print("Inside the phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")


class SmartPhone(Phone):
    def buy(self):
        print("Buying a Smartphone !")
        super().buy()  # super is used to access parent-class methods or constructors from a child class. It prevents code duplication and preserves inheritance behavior-  | this keyword cannot work outside the child class


"""
Using super keyword we can access only 2 thing from parent class to child class
access list:-
               Parent method
               Parent constructor 
access not possible :-
               Parent  attributes   
               
Parent class
______________
  class Phone:
    def __init__(self, price):
        self.__price = price    # private attribute

    def show_price(self):
        print("Price:", self.__price)
        
        
Child class
____________
  class SmartPhone(Phone):
    def __init__(self, price):
        super().__init__(price)   #  Parent constructor (1st statement after the constructor )

    def buy(self):
        super().show_price()      #  Parent method



 Access NOT possible (parent attribute)
____________________________________________
class SmartPhone(Phone):
    def get_price(self):
        print(super().__price)   #  ERROR


if we want to use super keyword we need to use it at the fast statement after the constructor 
"""

s = SmartPhone(10000, "apple", 48)
s.buy()
