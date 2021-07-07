# To kick us off we create a function that will add one to a number whenever it is called

# 1.Assigning Functions to Variables :
def plus_one(number) :
    return number+1
add_one=plus_one
print(add_one(5))

# o/p : 6

# 2.Defining Functions Inside other Functions
def plus_one(number) :
    def add_one(number) : 
        return number+1
    result= add_one(number)
    return result
print(plus_one(7))

# o/p : 8