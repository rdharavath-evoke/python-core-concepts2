'''
A tuple is a collection of multiple items in an ordered manner.
Tuples are sequences denoted by parenthesis () and placing the items inside a tuple can be of different types such as integer, string, float, list etc.,
The main charecteristic of tuple is that it is immutable.
Once a tuple has been assigned values, we cannot modify it.
We can reassign new values to a tuple but cannot change its individual items. 
Tuple comprehension cannot be directly performed in python, but there are other alternatives to it.
'''

# If we want to change tuple, first assign to list then change
a=[1,2,3,4,5,6,7,8]
l=list(a)
print(l)
# o/p : [1, 2, 3, 4, 5, 6, 7, 8]
l.append(20)
print(l)
# o/p : [1, 2, 3, 4, 5, 6, 7, 8, 20]
l.insert(2,55)
print(l)
# o/p : [1, 2, 55, 3, 4, 5, 6, 20]

l.extend([33,44])
print(l)
# o/p : [1, 2, 55, 3, 4, 5, 6, 20, 33, 44]

# 1.Concatination
a=(1,2,3)
b=(4,5,6)
print(a+b)
# o/p : (1, 2, 3, 4, 5, 6)

# 2.Repitition
print(a*2)
# o/p : (1, 2, 3, 1, 2, 3)
print(a*3)
# (1, 2, 3, 1, 2, 3, 1, 2, 3)

# *** print(a*b) : error accured
