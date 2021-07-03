list=[]
for letters in 'python programming' :
    list.append(letters)
print(list)
# o/p : ['p', 'y', 't', 'h', 'o', 'n', ' ', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']

list=[ele for ele in 'python']
print(list)
# o/p : ['p', 'y', 't', 'h', 'o', 'n']


a=[ele for ele in range(10)]
print(a)
# o/p : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

a=[ele*ele for ele in range(10)]
print(a)
# o/p : [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

a=[ele*ele for ele in range(10) if ele%2==0]
print(a)
# o/p : [0, 4, 16, 36, 64]



import time
# define function to implement for loop 
def for_loop(n):
    result=[]
    for i in range(n) :
        result.append(i**2)
    return result
# define function to implement for Comprehension
def comprehension(n) :
    return [i**2 for i in range(n)]

# driver code
# Calculate time-taken by for_loop
begin=time.time()
for_loop(10**6)
end=time.time()
print("time taken by for_loop", round(end-begin,2))
# Calculate time-taken by comprehension
begin=time.time()
comprehension(10**6)
end=time.time()
print("time taken by comprehension", round(end-begin,2))

# o/p : time taken by for_loop 0.38
# o/p : time taken by comprehension 0.32


###### Nested loop
matrix=[]
for i in range(4):
    matrix.append([])
    for j in range(4):
        matrix[i].append(j)
print(matrix)

# o/p : [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]

###### Nested list comprehension
matrix=[ [j for j in range(5)] for i in range(3)] 
print(matrix)

# o/p : [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]

##### Reverse each string in tuple
list=[string[::-1] for string in ("hello","python","program")]
print(list)
# o/p : ['olleh', 'nohtyp', 'margorp']

