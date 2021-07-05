# Python code to demonstrate dictionary comprehension

# Lists to represent keys and values
keys=['a','b','c','d','e']
values=[1,2,3,4,5]

#but this line shows dict comprehension here
myDict = { k:v for (k,v) in zip(keys,values)}

#We can use below too
#Mydict =dict(zip(keys, values))
print(myDict)

# o/p : {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Python code to demonstrate dictionary
# creation using list comprehension

myDict = {x: x**2 for x in [1,2,3,4,5]}
print(myDict) 

# o/p : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

sDict={x.upper():x*3 for x in 'Python'}
print(sDict)

# o/p : {'P': 'PPP', 'Y': 'yyy', 'T': 'ttt', 'H': 'hhh', 'O': 'ooo', 'N': 'nnn'}

newdict = {x : x**3 for x in range(10) if x**3 %4 ==0}
print(newdict)

# o/p : {0: 0, 2: 8, 4: 64, 6: 216, 8: 512}