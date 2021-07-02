# In many programming language there are 2-types of possible errors
'''
1.syntax error: The errors which occurs because of invalid syntax
2.runtime error: while excuting the program, at runtime something goes wrong..

runtime error also known as exception
'''

y=10
#print(y/0)
# o/p : ZeroDivisionError: division by zero

x=200
if x/20 :
    print(x)
    #print(x))
# o/p : SyntaxError: unmatched ')'

def divide(x,y) :
    try :
        result=x//y
        print(result)
    except ZeroDivisionError :
        print("error occured")
divide(3,0)
# o/p : error occured

def arith(a , b) :
    try:
        c=((a+b)/(a-b))
    except ZeroDivisionError:
        print("a/b result 0")
    else:
        print(c)
arith(2.0 , 3.0)
arith(3.0 , 3.0)
'''
o/p :
-5.0
a/b result 0
'''
def sum(a,b,c,d) :
    try:
        if a>b and a>c :
            print(a-b-c)
        elif b>c and b>c :
            print(b-c-a)
        elif c>a and c>b :
            print(c/a)
    except ZeroDivisionError :
        print("error")
    else :
        print("d")
    finally :
        print("there is no result")
sum(0,3,6,7)
        
'''
error
there is no result
'''