#write to a file call john doe.txt
#it should contain data about John doe
f=open("John doe.txt","w")
string='''
john doe is a good guy , 
top free fire player & python dev'''
f.write(string)
f.close()