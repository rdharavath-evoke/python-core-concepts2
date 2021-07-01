#Python supports the usual logical conditions from mathematics
#(a==b,a!=b,a<b,a<=b,a>b,a>=b.....)

# 1.if statement (if statement, without indentation (will raise an error))
a=20
b=40
if b>a:
    print("b is greater than a")
# o/p : b is greater than a
if b<a:
    print("b is less than a")
# o/p : (No output because condition is false)

# 2.else statement
a=30
b=20
if b>a:
    print("b is greater than a")
else :
    print("b is less than a")
# o/p : b is less than a

# 3.elif statement
a=30
b=30
if b>a:
    print("b is greater than a")
elif b<a :
        print("b is less than a")
else:
    print("a is equal to b")
# o/p : a is equal to b

# 4.Short hand if
a=50
b=40
if a>b : print("a is greater than b")
# o/p : a is greater than b

# 5.Short hand if ... else
a=10
b=5
print("a") if a > b else print("b")
# o/p : a

a=10
b=10
print("a") if a > b else print("a=b") if a==b else print("b") 
# o/p : a=b

# 6.and
a=53
b=44
c=75
if a>b and a>c :
    print("a is greatest")
elif b>c and b>a :
    print("b is greatest")
else :
    print("c is greatest")
    
# o/p : c is greatest

# 7.or
a=53
b=88
c=14
if a>b or a>c :
    print("atleast one of the conditions is True")
# o/p : atleast one of the conditions is True

# 8.Nested if
a=30
print("Given a=30")
if a>10 :
    print("a>10 : Yes")
    if a>20 :
        print("a>20 : Yes")
    else :
        print("No")

# o/p : Given a=30
#       a>10 : Yes
#       a>20 : Yes

# 9.pass (Having an empty statement like this, would raise an error without the pass stmt)
a=200
b=300
if b>a :
    pass

# 10.while
x=1
while(x<5) :
    print(x, end= " ")
    x=x+1
print()
# o/p : 1 2 3 4

# 11.Nested while loop
i=5
j=0
while i>0 :
     while j<5 :
         print(i,j)
         i=i-1
         j=j+1
'''
# o/p :
5 0
4 1
3 2
2 3
1 4
'''

# 12.for
for i in range(1,10) :
    print(i, end=" ")
print()
# o/p : 1 2 3 4 5 6 7 8 9

a=[i*i for i in range(0,10)] 
print(a)
# o/p : [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

a={i*i for i in range(0,10) if i%2==0} 
print(a)
# o/p : {0, 64, 4, 36, 16}
