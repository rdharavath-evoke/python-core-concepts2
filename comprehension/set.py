'''
Set comprehensions are pretty similar to list comprehensions.
The only difference between them is that set comprehensions use curly brackets {}.
'''

input_list = [1,2,3,4,4,5,6,6,6,7,7]
output_set=set()

# Using loop for constructing output set
for var in input_list:
    if var%2==0:
        output_set.add(var)
print("Output set using for loop : ", output_set)
# o/p : {2, 4, 6}

# Using Set comprehensions for constructing output set
a=[2,4,4,4,5,3,3,3,6,6,6,66,7,7,77,77]
b={i for i in a if i%2==0}
print(b)
# o/p : {2, 4, 66, 6}