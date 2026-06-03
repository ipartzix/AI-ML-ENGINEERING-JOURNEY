# It is a full flared ATM machine system design in oops code structure
# to understand the concept of Object-Oriented-Programming


class Atm:
    # static/class
    __counter = 1  # this type of thing always out of the constructor but under the class

    def __init__(self):
        # instance variable :-it is a kind of variable for which the value of the variable is different for different object

        # __init__ is a constructor // Constructor is a special method  ,< self > always run itself
        # self is the object that we are working right now
        # for our case we create an object name is sbi [ sbi = Atm() ]


        self.__pin = ""  # hide the data using Double underscore (__) *****Encapsulation
        self.__balance = 0  # hide the data using Double underscore (__) *****Encapsulation
        # Nothing in python truly private
        self.sno = Atm.__counter
        Atm.__counter = Atm.__counter + 1  # make counter encapsuled
        # always add one when the object will call it
        print(id(self))

        self.__menu()

    @staticmethod
    def get_counter():
        return Atm.__counter

    @staticmethod

    def set_counter(new):
        if type(new) == int:
            Atm.__counter = new
        else:
            print("Not Allow")

        def get_pin(self):
            return self.__pin

        def set_pin(self, new_pin):
            self.__pin = new_pin
            print("pin changed successfully !")



    # one method can not access with another method directly they take help of object
    # so for every method self do this job the object is pass through self and without self the code show error

    def __menu(self):
        while True:
            user_input = input(
                """ 
                Hello , how would like to proceed ?
                1.Enter to create pin 
                2.Enter to deposit 
                3.Enter to withdraw 
                4.Enter to check balance 
                5.Enter to exit
        """)

            # always write logic inside the method
            # I have make mistake hare , I write the logical loop function outer the method so the   class don't access it and give me error

            if user_input == "1":  # Fixed: comparing string to string
                self.create_pin()  # object_name + Method-name( self is object and create pin is a method)
            elif user_input == "2":
                self.deposit()
            elif user_input == "3":
                self.withdraw()
            elif user_input == "4":
                self.check_balance()
            elif user_input == "5":
                print("Bye ")
                break
            else:
                print("invalid input")

    # for creating pin for new user
    def create_pin(self):
        self.__pin = input("Enter pin : ")
        print("Pin created Successfully !")

    # for deposit money
    def deposit(self):
        temp = input("Enter your pin : ")
        if temp == self.__pin:
            amount = int(input("Enter amount : "))
            self.__balance = self.__balance + amount
            print("Deposit successful "
                  "Your balance is: ", self.__balance)
        else:
            print("Invalid pin !")

    #for withdraw money
    def withdraw(self):
        temp = input("Enter your pin : ")
        if temp == self.__pin:
            amount = int(input("Enter amount : "))
            if self.__balance >= amount:
                self.__balance = self.__balance - amount
                print("withdraw successful  "
                      "Your balance is: ", self.__balance)
            else:
                print("insufficient balance !")
        else:
            print("Invalid pin !")

    # for balance chacking
    def check_balance(self):
        temp = input("Enter your pin: ")  #input always take as string
        if temp == self.__pin:
            print(f"Your balance is: {self.__balance}")
        else:
            print("Invalid pin!")


# Creating an object of the class
sbi = Atm()
