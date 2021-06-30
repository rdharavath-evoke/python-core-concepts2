#importing "array" for array creations
import array as arr

#creating an array with integer type
a=arr.array('i', [1,2,3,4,5,6])
#printing original array
for i in range(0,6) :
    print(a[i],end=" ")
print()

# o/p : 1 2 3 4 5 6

#creating an array with float type
a=arr.array('d', [1.4,2.5,3.0,4.4])
#printing original array
for i in range(0,4) :
    print(a[i],end=" ")
print()

# o/p : 1.4 2.5 3.0 4.4

a=arr.array('i', [1,2,3,4,5,6])
#printing original array
for i in range(0,6) :
    print(a[i],end=" ")
print()
# o/p : 1 2 3 4 5 6

# 1.insertion
a.insert(2,8)
a.insert(4,55)
for i in (a):
    print(i,end=" ")
print()
# o/p : 1 2 8 3 55 4 5 6

# 2.append
a.append(66)
for i in (a):
    print(i,end=" ")
print()
# o/p : 1 2 8 3 55 4 5 6 66

# 3.accessing
print(a[0])
# o/p : 1

# 4.remove or pop
a.remove(1)
for i in (a):
    print(i,end=" ")
print()
# o/p : 2 8 3 55 4 5 6 66
a.pop(3)
for i in (a):
    print(i,end=" ")
print()
# o/p : 2 8 3 4 5 6 66

# 5.slicing
print(a[2:4])
# o/p : array('i', [3, 4])

# 6.index
a=arr.array('i', [1,2,3,4,55,6])
#printing original array
for i in range(0,5) :
    print(a[i],end=" ")
print()
print(a.index(55))
# o/p : 4