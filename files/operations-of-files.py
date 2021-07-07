
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