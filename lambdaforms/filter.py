from typing import Sequence
import logging

def fun(variable):
    letters=['a','e','i','o','u']
    if (variable in letters):
        return True
    else:
        return False

sequence=['g','e','f','a','k','m','e']
filtered=filter(fun,sequence)
logging.info("The filtered letters are :")
for s in filtered:
    print(s)

seq=[0,1,2,3,4,5,8,13,22]
result=filter(lambda x:x%2!=0, seq)
print(list(result))
result=filter(lambda x:x%2==0, seq)
print(list(result))
result=filter(lambda x: 2*x, seq)
print(list(result))