print("please select the option tha ta you want")
print("1= add")
print("2= sub")
print("3= mul")
print("4= div")
print("5= exit")
a =int(input("enter the 1st number:"))
b =int(input("enter the 2nd number:"))
choice=int(input("enter the choice:"))
if choice==1:
    print(a+b)
elif choice==2:
    print(a-b)
elif choice==3:
    print(a*b)
elif choice==4:
    print(a/b)
else:
    print("invalid choice")
print("thank you")