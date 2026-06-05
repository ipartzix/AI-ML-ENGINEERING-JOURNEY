# print("Welcome to Python If else statement question ")
# age =int (input("Enter a number: "))

# if age >= 100:
#     print("take rest ")

# elif 19<= age >= 60:
#     print("Your age is greater than or equal to 60")

# elif 59>= age >=18:
#     print("Your age is greater than or equal to 18")

# else :
#     print("Your age is less than or equal to 18")


print("Welcome to Python If-Else Logic")
age = int(input("Enter a number: "))

if age >= 100:
    print("take rest")
elif age >= 60:
    # If the code reaches here, it means age is < 100
    print("Your age is greater than or equal to 60")
elif age >= 18:
    # If the code reaches here, it means age is < 60
    print("Your age is greater than or equal to 18")
else :
    # If the code reaches here, it means age is < 18
    print("Your age is less than 18")