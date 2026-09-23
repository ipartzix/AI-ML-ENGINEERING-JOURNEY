"""
        5
      5 4
    5 4 3
  5 4 3 2 
5 4 3 2 1

"""
p = int(input("Enter a number :-"))

for i in range(1,p+1):
    for s in range(p-i):
         print(" ",end=" ")
    for n in range(p,p-i,-1):
         print(n,end=" ")
    print()