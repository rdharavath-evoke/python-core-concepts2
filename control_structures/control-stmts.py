#Loop control statements change execution from its normal sequence
#Python supports the following control statements

# 1.continue
for letter in 'python_programming' :
    if letter=='o' or letter=='m' :
        continue
    print(letter, end=" ")
print()
# o/p : p y t h n _ p r g r a i n g

x=1
while(x<15) :
    if x==3 or x==5 :
        x=x+1
        continue
    else:
     print(x,end=" ")
     x=x+1
print()
# o/p : 1 2 4 6 7 8 9 10 11 12 13 14


# 2.break
for letter in 'python_programming' :
    if letter=='o' :
        break
    print(letter, end=" ")
print()
# o/p : p y t h

x=1
while(x<10) :
    if x==11 :
        x=x+1
        break
    else:
     print(x,end=" ")
     x=x+1
print()
# o/p : 1 2 3 4 5 6 7 8 9 10

# 3.pass

# 9.pass (Having an empty statement like this, would raise an error without the pass stmt)
a=200
b=300
if b>a :
    pass