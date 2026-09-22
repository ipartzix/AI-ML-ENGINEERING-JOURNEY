s = {2, 44, 55, 777}
print(s, type(s))
# print(s[2])#we can not access set by using the index number bcz it store the element in random way
print(s)
s.add(99)
print(s)
s.pop()  # removes a random element
print(s)
s.pop()  # removes a random element
print(s)
s.pop()  # removes a random element
print(s)
s.pop()  # removes a random element
print(s)
s.pop()  # removes a random element
print(s)
# #in the case of removing it maybe the 1st element of the string one by one
s.discurd(333)

# the out put of this isss

# {777, 2, 44, 55} <class 'set'>
# {777, 2, 44, 55}
# {2, 99, 777, 44, 55}
# {99, 777, 44, 55}
# {777, 44, 55}
# {44, 55}
# {55}
# set()

a = {33, 32, 44, 66}
b = {44, 67, 78}
c = a.union(b)
print(c)
c = a.intersection(b)
print(c)
