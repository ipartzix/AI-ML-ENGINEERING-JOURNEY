#write to a file call john doe.txt
#it should contain data about John doe
f=open("John doe.txt","a")
string='''\nMaster Python Programming from Scratch: Build Real-World Projects and Become Job-Ready in 2025'''
f.write(string)
f.close()
print("Done")