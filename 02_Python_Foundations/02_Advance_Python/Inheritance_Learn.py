class User:

    def login(self):
        print("Login")

    def register(self):
        print("Register")


class Student(
    User):  # in student class we use "(User) inside the  student class that inherit thr property of parent class
    # student can use user class but user can not use student class

    def enroll(self):

        print("Enroll")

    def review(self):
        
        print("course review ")


stu1 = Student()

stu1.enroll()
stu1.review()
stu1.login()
stu1.register()


class Phone:
    def __init__(self, price, brand, model):
        self.price = price
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"brand={self.brand},model={self.model} and price is {self.price} ,"


# child class can not use or access parent class hidden member can not access

class SmartPhone(Phone):
    pass


s = SmartPhone(100000, "apple", "17 PRO MAX")
print(s)

# when 2 or more method are available in parent and child both class it always run child class method  it called method overwriting
