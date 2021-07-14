print("function for even or odd : ")
def evenOdd(x):
    if x%2==0 :
        print('even')
    else:
        print("odd")
evenOdd(5)
evenOdd(8)

print("\nDocument String")
def say_Hi():
    "hello! raman!"
print(say_Hi.__doc__)

print("\nThe return statement : ")
def squarevalue(a):
    return a**2
print(squarevalue(5))
print(squarevalue(7))

print("\nPass by value or pass by reference : ")
def myFun(x):
    x[0]=100
list=[10,20,30,40,59]
myFun(list)
print(list)

def myFun(x):
    x=20
x=10
myFun(x)
print(x)
print(myFun)

print("\nswapping : ")
def swap(x, y):
    temp=x
    x=y
    y=temp
    print(x,y)
swap(2,7)

print("\ndefault arguments :")
def fun(x, y=30):
    print('x=',x)
    print('y=',y)
fun(50)

print("\nKeyword arguments : ")
def student(first_name,last_name):
    print("first_name=",first_name)
    print("last_name=",last_name)
student(first_name='Rama',last_name="Swamy")

print("\nvariable length argument : ")
def myFunc(*argv):
    for arg in argv :
        print(arg)
myFunc('hello', 'welcome', 'to', 'python')

print('\nAnonymous functions : ')
def cube(x): return x*x*x
cube_x=lambda x : x*x*x
print(cube(5))
print(cube_x(5))

