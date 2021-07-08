
# 1.open and read
f=open("D:/textfiles.txt","r")
a=f.read()
print(a)
f.close()

# 2.open and write

f=open("D:/textfiles.txt","w")
f.write(" python is a best language")
f.close()

# 3.open and append

f=open("D:/textfiles.txt","a")
f.write(" \nIt is mainly used for mobile application")
f.close()


try:
    f=open("D:/textfiles.txt","r")
    print(f.read())
except:
    print("file not exist")

#### Program to show various ways to read and write data in a file

file1=open("D:/myfile.txt","w")
a=["This is Hyderabad\n","This is Mumbai\n","This is Delhi"]
file1.write("hello Python\n")
file1.writelines(a)
file1.close()

file1=open("D:/myfile.txt","r+")
print("Output of read function is")
print(file1.read())

# o/p : 
'''
Output of the read function is
hello Python
This is Hyderabad
This is Mumbai
This is Delhi
'''
