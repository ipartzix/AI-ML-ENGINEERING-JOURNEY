# WB3231698648039
# paulPartha@2005
class Employee:
    company="HP"

    def get_salary(self):#self is important here because self is a way to reference the object of the class which is being created
        return 35000
e=Employee()# an object of class employee is created here
print(e.get_salary())#employee e's get salary method is called here
e2=Employee()
print(e.get_salary())
print(e.company)
print(e2.company)