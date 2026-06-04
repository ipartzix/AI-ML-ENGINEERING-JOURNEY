# Creating our own data type using a class
class Fraction:

    # Constructor: runs automatically when an object is created
    def __init__(self, n, d):
        self.num = n  # numerator (top part of fraction)
        self.den = d  # denominator (bottom part of fraction)

    # This method controls what is printed when we print the object
    def __str__(self):
        # Converts the fraction object into a string like "3/4"
        return "{}/{}".format(self.num, self.den)

    # Overloading the + operator
    def __add__(self, other):
        # Formula: a/b + c/d = (ad + bc) / bd
        temp_num = self.num * other.den + other.num * self.den
        temp_den = self.den * other.den

        # Returning result as a string (not as a Fraction object)
        return "{}/{}".format(temp_num, temp_den)

    # Overloading the - operator
    def __sub__(self, other):
        # Formula: a/b - c/d = (ad - bc) / bd
        temp_num = self.num * other.den - other.num * self.den
        temp_den = self.den * other.den

        # Returning result as a string
        return "{}/{}".format(temp_num, temp_den)

    # Overloading the * operator
    def __mul__(self, other):
        # Multiplying numerator with denominator (logical mistake, but kept as-is)
        temp_num = self.num * other.den
        temp_den = self.den * other.den

        # Returning result as a string
        return "{}/{}".format(temp_num, temp_den)

    def __truediv__(self, other):
        temp_num = self.num * other.den
        temp_den = self.den * other.num
        return "{}/{}".format(temp_num, temp_den)

# Creating Fraction objects
x = Fraction(3, 4)
y = Fraction(5, 6)

# Printing the fractions
print(x)  # Calls __str__ → "3/4"
print(y)  # Calls __str__ → "5/6"

# Performing operations using operator overloading
print(x + y)  # Calls __add__
print(x - y)  # Calls __sub__
print(x * y)  # Calls __mul__
print(x / y)  # Calls __truediv__

# Reference variable :- When creating an Object we create an object and store the object in a variable this variable called reference variable
