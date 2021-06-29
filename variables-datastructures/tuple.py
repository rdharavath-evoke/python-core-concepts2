#Tuple is immutable 
#There is no permission to change after the tuple creation
a=(1,2,3,4,5,6)
print(a)
print(a[4])
# o/p : 5

print(a[-1])
# o/p :  8

print(a[3:6])
# o/p : (4, 5, 6)

# If we want to change tuple, first assign to list then change
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

# 3.Length of tuple
a=(1,2,3,4,5,6,7)
print(len(a))
# o/p : 7

# 4.Min and Max of tuple
print(min(a))
# o/p : 1
print(max(a))
# o/p : 7

# 5.Sum of tuple
print(sum(a))
# o/p : 28

# 6.Membership of ele
a=(22,34,56,78,54,25,73,85)
print(22 in a)
# o/p : True
print(55 in a)
# o/p : False


