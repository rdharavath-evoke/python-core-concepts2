a=[22,49,34,44,53,64,25,34,77]
b=[ 2*i for i in range(len(a)) ]
print(b)
# o/p : [0, 2, 4, 6, 8, 10, 12, 14, 16]

a=[22,49,34,44,53,64,25,34,77]
b=[a[i] for i in range(len(a)) if i%2==0]
print(b)
# o/p : [22, 34, 53, 25, 77]