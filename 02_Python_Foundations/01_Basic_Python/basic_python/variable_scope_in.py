#function scoping
def sum(a, b):
    # a and b are local variables
    c = a + b
    z = 1  # It creates a local variable called z which is destroyed after this function returns
    return c




def greet():
    z = 32  # Local variable
    print("Hello")


z = 8  # z is a global variable
print(z)
print(sum(4, 6))
print(z)


#global
def sum(a, b):
    print("Hey I am summing ")
    c = a + b
    global z # Please modify global z
    z = 0 # This will refer to global z and not create a local variable
    return c

z = 3
print(sum(3, 12))
print(z)

