import logging
import functools
logging.basicConfig(level=logging.DEBUG)
logging.info("arithmetic operations")
def operation(n):
    return n+n,n*n,n/n,n%n
numbers=[1,2,3,4,5]
result=map(operation,numbers)
logging.debug(list(result))

numbers1=[1,2,3,4,5]
numbers2=[6,7,8,9,6]
result=map(lambda x,y : x*y,numbers1,numbers2)
logging.debug(list(result))

l=['sat','mat','rat']
test=list(map(list, l))
logging.debug(test)

def square(number):
    if number%2==0:
        return number**2
    elif number==2:
        return number+number
    else:
        return number/2
numbers=[1,2,3,4,5,6]
squared=map(square,numbers)
logging.debug(list(squared))


list_=[1,3,5,6,7,9,2]
logging.debug("sum of the list elements is :")
logging.debug(functools.reduce(lambda a,b:a+b,list_))
logging.debug("The maximum element in the list :")
logging.debug(functools.reduce(lambda a,b : a if a>b else b, list_))