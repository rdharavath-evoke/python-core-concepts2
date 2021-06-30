#Set have coma superated values
#Multiple datatypes is allowed 
#If Set have Duplicate values that will be removed
#Unordered
#Unique
#Mutable
#### No slicing and No Indexing
s={}
print(type(s))
# o/p : <class 'dict'>

s=set()
print(type(s))
# o/p : <class 'set'>

s={10,20,30,40}
print(s)
# o/p : {40, 10, 20, 30} ##unordered

s={10,20,30,20,30,10,20,10}
print(s)
# o/p : {10, 20, 30} ##duplicates are not allowed

print(len(s))
# o/p : 3

s={10,20,30}
s.add(40)
print(s)
# o/p : {40, 10, 20, 30}

s.remove(30)
print(s)
# o/p : {40, 10, 20}

s.discard(100)
print(s)
# o/p : {40, 10, 20}

s.clear()
print(s)
# o/p : set()

s={10,20,30,40}
print(20 in s)
# o/p : True

for ele in s :
    print(ele,end=" ")
    print()
# o/p : 40 10 20 30

s={10,20,30}
t={10,20,30,40,50,60}
print(s.issubset(t))
# o/p : True

print(t.issuperset(s))
# o/p : True

print(s.union(t))
# o/p : {40, 10, 50, 20, 60, 30}

print(s.intersection(t))
# o/p : {10, 20, 30}

print(t.difference(s))
# o/p : {40, 50, 60}

print(s.symmetric_difference(t))
# o/p : {50, 40, 60}

s={10,20,30,100}
t={10,20,30,40,50,60}
s.update(t)
print(s)
# o/p : {100, 40, 10, 50, 20, 60, 30}

s.intersection_update(t)
print(s)
# o/p : {40, 10, 50, 20, 60, 30}

t.difference_update(s)
print(t)
# o/p : set()
print(s)
# o/p : {40, 10, 50, 20, 60, 30}

t.symmetric_difference_update(s)
print(t)
# o/p : {40, 10, 50, 20, 60, 30}

s={1,2,3,4,5}
t=s.copy()
print(t)
# o/p : {1,2,3,4,5}
