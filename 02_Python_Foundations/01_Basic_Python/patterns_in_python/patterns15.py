"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 3 3 4 5
"""

for i in range(1, 6):
    for j in range(1, 6):
        print(j, end=" ")
    print()


for i in range(1, 6):
    for j in range(1, 6):
        if i == 5 and j == 2:
            print(3, end=" ")
        else:
            print(j, end=" ")
    print()
