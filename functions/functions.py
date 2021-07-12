'''
We will see how to write our own functions, which is a great way to avoid duplicating code.
Putting code in a function allows you to use it over and over again, without re-writing it.
We will also learn about returning values from functions.
Not all functions return a useful value. Some functions, like print, and the .sort method of lists, perform an action.
# print prints something out. When you use sort it sorts the list. These functions don't return anything useful.
Other functions calculate a value, and return for your main code to use.
We will look at the difference, in this section, and see how to write both types of functions

'''
# a simple program to multiply two numbers using function
def multiply():
    result=4.5*3
    return result

answer=multiply()
print(answer)

#using paranthesis
def multiply(a,b):
    result=a*b
    return result

answer=multiply(5,6)
print(answer)
thirty=multiply(10,3)
print(thirty)
print()

for val in range(1,5):
    two_times=multiply(2,val)
    print(two_times)

# o/p :
'''
13.5
30
30

2
4
6
8
'''

def is_palindrome(string):
    #backwards=string[::-1]
    #return backwards==string
    return string[::-1]==string

word=input("please enter a word to check  ")
if is_palindrome(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))

# o/p : 'racecar' is a palindrome
# o/p : 'Radar' is not a palindrome

def is_palindrome(string):
    #backwards=string[::-1]
    #return backwards==string
    return string[::-1].casefold()==string.casefold()

word=input("please enter a word to check  ")
if is_palindrome(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))

# o/p : Radar is a palindrome

# python program to find if a sentence is Palindrome
# To check sentence is palindrome or not 
print()

def palindrome(string):
    first=0
    last=len(string)-1
    status=1
    while(last>=first):
        if(string[first]==string[last]):
            first=first+1
            last=last-1
        else:
            status=0
        return status
string=input("enter the string : ")
status=palindrome(string)
if status==1 :
    print("The given string is palindrome")
else:
    print("The given string is not palindrome")

# o/p : 
'''
enter the string : radar
The given string is palindrome
'''



# scope and lifetime of variables

def my_fun():
    x=100
    print("the value inside function",x)
x=200
my_fun()
print("the value outside function",x) # o/p : the value outside function 200
x=my_fun()
print("the new value of x : ",x) #o/p : the new value of x : None
    
# Arbitary Arguments: *args,**args and keywords
def fun1(*kids):

    def fun2(**kids):

        def fun3(child1,child2,child3):
            print("The youngesh child is "+child3)
        fun3(child1="vijay",child2="Manish",child3="Shiva")
        
        print("His last name is ",kids['lname'])
    fun2(fname='sahu',lname='sanjay')
    
    print("The oldest child is ",kids[2])
fun1("manu","siri","Hari")

