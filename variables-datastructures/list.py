#Unlike c++ or Java, 'Python' Programming Language doesn't have arrays. 
#To hold a sequence of values, then, Python provides the 'list' class.
a=[10,20,30,40,50]
print(a)
# o/p : [10,20,30,40,50]
print(a[0])
#o/p : 10
a=[]
print(a)
#o/p : []  :::empty list
print(type(a))
# o/p : <class 'list'>

a=[10,2.44,"hello"]
print(a)
#o/p : [10, 2.44, 'hello']

#list is Mutable
#we have the option to change after creating the list
print(a[0])
# o/p : 10
print(a[-2])
# o/p :2.44
print(a[-1])
# o/p : 'hello'

####  Slicing in List #####


a=[10,20,30,40,50,60]
print(a[:])
# o/p : [10,20,30,40,50,60]

print(a[3:])
# o/p : [40,50,60]

print(a[-2:-5])
# o/p : []
print(a[-5:-2])
# o/p : [20, 30, 40]


######## Re-assigning the list elements  #########
a=[3.3,4,5,6.6,"hi",7,'hello']
print(a)
# o/p : [3.3, 4, 5, 6.6, 'hi', 7, 'hello']

a[3]=6
a[4]=2
a[0]=3
a[6]=9

print(a)
# o/p : [3, 4, 5, 6, 2, 7, 9]

##########  2-Dimantional List  ########
a=[[2,3],3,[4,5,6],7,8,9]
print(a)
# o/p : [[2, 3], 3, [4, 5, 6], 7, 8, 9]

print(a[0])
# o/p : [2,3]

print(a[2])
# o/p : [4,5,6]

print(a[4])
# o/p : 8

print(a[2][1])
#o/p : 5

######   3-Dimantional List  ########

a=[  [[1,2,3],[4,5]],  [[6,7,8],[9,10,11]]   ]
print(a[1])
# o/p : [[6, 7, 8], [9, 10, 11]]

print(a[1][1])
# o/p : [9, 10, 11]

print(a[1][1][1])
# o/p : 10

############# Basic Operations #################

# 1.Concatination
a=[1,2,3]
b=[4,5,6]
print(a+b)
# o/p : [1, 2, 3, 4, 5, 6]

# 2.Repitition
print(a*2)
# o/p : [1, 2, 3, 1, 2, 3]
print(a*3)
# [1, 2, 3, 1, 2, 3, 1, 2, 3]

# *** print(a*b) : error accured

# 3.Length of List
a=[1,2,3,4,5,6,7]
print(len(a))
# o/p : 7

# 4.Min and Max of list
print(min(a))
# o/p : 1
print(max(a))
# o/p : 7

# 5.Sum of list
print(sum(a))
# o/p : 28

# 6.Membership of ele
a=[22,34,56,78,54,25,73,85]
print(22 in a)
# o/p : True
print(55 in a)
# o/p : False

# 7.Iteration
b=[ 2*i for i in range(len(a)) ]
print(b)
# o/p : [0, 2, 4, 6, 8, 10, 12, 14]

a=[22,49,34,44,53,64,25,34,77]
b=[a[i] for i in range(len(a)) if i%2==0]
print(b)
# o/p : [22, 34, 53, 25, 77]

########### Built in methods ########

# 1.append
a=[3,4,5,6]
a.append(7)
print(a)
# o/p : [3, 4, 5, 6, 7]

# 2.insert
a=[3,4,5,6]
a.insert(3,22)
print(a)
# o/p : [3, 4, 5, 22, 6]

# 3.extend
a=[3,4,5,6]
a.extend([55,44])
print(a)
# o/p : [3, 4, 5, 6, 55, 44]

# 3.delete
a=[3,4,5,6]
a.pop(2)
print(a)
# o/p : [3, 4, 6]
del(a[0])
print(a)
# o/p : [4, 6]

# 4.Sorting
a=[99,55,23,62,18,41]
a.sort()
print(a)
# o/p : [18, 23, 41, 55, 62, 99]

a.sort(reverse=True)
print(a)
# o/p : [99, 62, 55, 41, 23, 18]

# 5.Count
a=[99,55,23,55,18,41,55,55]
print(a.count(55))
# o/p : 4
 
# 6.index
a=[99,55,23,55,18,41,55,55]
print(a.index(23))
# o/p : 2

# 7.reverse
a=[99,55,23,55,18,41,55,55]
a.reverse()
print(a)
# o/p : [55, 55, 41, 18, 55, 23, 55, 99]


# 8.List Comprehension
a=[ele for ele in range(10)]
print(a)
# o/p : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

a=[ele*ele for ele in range(10)]
print(a)
# o/p : [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

a=[ele*ele for ele in range(10) if ele%2==0]
print(a)
# o/p : [0, 4, 16, 36, 64]

