class Employee:
    company = "HP"

    # Constructor with parameters
    def __init__(self, salary, name, experience):
        self.salary = salary
        self.name = name
        self.experience = experience

    def get_salary(self):
        return self.salary

# Creating an object with arguments
e1 = Employee(35000, "Shyam", 4)


# Accessing method and attributes
print("Name:", e1.name)
print("Salary:", e1.get_salary())
print("Experience:", e1.experience)
print("Company:", e1.company)
