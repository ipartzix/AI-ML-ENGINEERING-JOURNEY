# Q. Except an integer and print hellow world n time
# num = int (input("enter a number:-"))
# for i in range(num):
#     print("Hello World")

#Q. Print natural number upto n
# num =int(input("Enter a number: "))
# for i in range(1,num+1):
#     print(i)


#Q.Reverse a loop from n to 1
# num =int(input("Enter a number: "))
# for i in range(num,0,-1):
#     print(i)


#Q take a number and print its multiplication table
# num =int(input("Enter a number for get its multiplication table : "))
# for i in range(1,11):
#     print(f"{i} * {num} = {i*num} ")





#Q. Sum upto n terms
# n =int(input("Enter a number: "))
# summ =0
# for i in range(1,n+1,1):
#     summ += i
#     print(f"{i} and {summ} ")
# print(f"the sum is {summ}")




#Q Factorial of a number
# fact =int(input("Enter a number: "))
# f =1
# for i in range(1,fact+1):
#     f=f*i
#     print(f)
# print(f)




#Q. print all sum of odd and even number in separate in a user input range
# number = int(input("Enter a number: "))
# odd =0
# even =0
# for i in range(number+1):
#     if i % 2 != 0:
#         odd +=i
#     else :
#         even +=i
# print(f"For range 0 to {number}:")
# print(f"Sum of Odd numbers: {odd}")
# print(f"Sum of Even numbers: {even}")




# # Q. Print factors of all numbers up to n
# n = int(input("Enter the range: "))
#
# for i in range(1, n + 1):
#     print(f"Factors of {i}:", end=" ")
#     for j in range(1, i + 1):
#         if i % j == 0:
#             print(j, end=" ")
#     print() # Moves to a new line for the next number




# #Q. Corrected Perfect Number Logic
# number = int(input("Enter the number: "))
# summ = 0
#
# # Loop from 1 to number-1
# for i in range(1, number):
#     if number % i == 0:
#         summ = summ + i # Add the divisor 'i', don't just count it!
#
# if summ == number:
#     print(f"{number} is a Perfect Number")
# else:
#     print(f"{number} is NOT a Perfect Number")






# # check prime or not
# num = int(input("Enter a number to check prime or not: "))
# counter = 0
# for i in range(1, num+1):
#     if num % i == 0:
#         counter += 1
# if counter == 2:
#     print("Prime")
# else:
#     print("Not prime")





# #Q. Reverse a string without using inbuilt function
#
# a ="randumnumber"
# # print(a[::-1])
# b=""
# for i in range(len(a)-1,-1,-1):
#     b=b+a[i]
# print(b)




#Q. check a number palindrome or not
# a =str(input("Enter a string: "))
# # print(a[::-1])
# b=""
# for i in range(len(a)-1,-1,-1):
#     b=b+a[i]
# if(b==a):
#     print("its a palindrome number")
# else:
#     print("Not a palindrome")
#


# s = "kndjfnwipfcwrm3854345394-3q0/'ASX;A]"
# char = 0
# dig = 0
# spcr = 0
#
# for i in s:
#     if i.isdigit():
#         dig += 1
#     elif i.isalpha():
#         char += 1
#     else:
#         spcr += 1
#
# print(f"Characters: {char}")
# print(f"Digits: {dig}")
# print(f"Special Characters: {spcr}")
#
#
print("While loop")

# number= int(input("Enter a number: "))
# while 10>number>0:
#     print(int(number))
#     number =number+1


#separate each digit of a number and print it on the new line
# a = int(input("Enter a number: "))
# while a > 0:
#     digit = a % 10    # Gets the last digit (4, then 3...)
#     print(digit)      # Prints it on a new line
#     a = a // 10       # Removes the last digit (1234 -> 123)





# Accept a number and print its reverse
# a = int(input("Enter a number: "))
# reverse = 0
#
# while a > 0:
#     # 1. Get the last digit (Remainder)
#     remainder = a % 10
#
#     # 2. Append it to the reverse number
#     reverse = (reverse * 10) + remainder
#
#     # 3. Remove the last digit from 'a' using integer division
#     a = a // 10
#
# print("Reversed number:", reverse)