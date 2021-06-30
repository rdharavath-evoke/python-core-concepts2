#Dictionary is a key-value pair
#In place of keys, Duplicates are not allowed
#values may be duplicate
#Access : Indexing(key-index)

d={}
print(d)
# o/p : {}

print(type(d))
# o/p : <class 'dict'>

d={"name":"jay","age":20,"Branch":"cse"}
print(d)
# o/p : {"name":"jay","age":20,"Branch":"cse"}

# 1.accessing
print(d["name"])
# o/p : jay

# 2.update
d["college"]="MVSR"
print(d)
# o/p : {'name': 'jay', 'age': 20, 'Branch': 'cse', 'college': 'MVSR'}

d1={"name":"jay","age":20,"Branch":"cse"}
d2={"college":"MVSR","city":"Hyderabad"}
d1.update(d2)
print(d1)
# o/p : {'name': 'jay', 'age': 20, 'Branch': 'cse', 'college': 'MVSR', 'city': 'Hyderabad'}


# 3.length
print(len(d))
# o/p : 4

# 4.del
del d
# print(d)
# o/p : NameError: name 'd' is not defined

# 5.clear
d={"name":"jay","age":20,"Branch":"cse"}
d.clear()
print(d)
# o/p : {}

# 6.Comprehension
d={i:i**2 for i in range(10)}
print(d)
# o/p : {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

d={i:i**3 for i in range(10) if i%2==1}
print(d)
# o/p : {1: 1, 3: 27, 5: 125, 7: 343, 9: 729}

# 7.Nested dictionary
d={"name":{"fname":"jay","lname":"dhara"},"age":20,"Branch":"cse"}
print(d["name"])
# o/p : {'fname': 'jay', 'lname': 'dhara'}

print(d['name']['fname'])
# o/p : jay

# 8.copy
s=d.copy()
print(s)
# o/p : {"name":{"fname":"jay","lname":"dhara"},"age":20,"Branch":"cse"}
