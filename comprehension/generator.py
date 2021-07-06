'''
Generator Comprehensions are very similar to list comprehensions.
One difference between them is that generator comprehensions use circular brackets whare as list comprehensions use square brackets.
The major difference between them is that generators don't allocate memory for the whole list.
Instead, they generate each value one by one which is why they are memory efficient.
'''

input=[1,2,2,3,4,4,4,5,6,6,6,6,7,7]
output=(i for i in input if i%2==1)
print("Output values using generators comprahensions : ",end='')
for i in output :
    print(i, end=' ')

# o/p : 1 3 5 7 7