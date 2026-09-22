# Create a list containing the table of a given number
num = int(input("Enter the number for the table you want: "))

# Method 1: Using a for loop
table = []
for i in range(0, 11):
    table.append(num * i)
print("The table using loop is:", table)

# Method 2: Using list comprehension
table = [num * i for i in range(0, 11)]
print("The table using list comprehension is:", table)
