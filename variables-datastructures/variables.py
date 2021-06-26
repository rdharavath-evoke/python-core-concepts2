#Think of a variable as a name attached to a particular object
n=300
print(n)
# o/p : 300
#Python also allows chained assignment
#which makes it possible to assign the same value to several variables simultaneously
a=b=c=200
print(a,b,c)
# o/p : 200 200 200
#In many programming languages, variables are statically typed
#Variables in Python are not subject to this restriction
var=23.66
print(var)
# o/p : 23.66
var="Now I'm a string"
print(var)
# o/p : Now I'm a string

#The following code verifies that points to an integer object :
print(n)
# o/p : 300
print(type(n))
# o/p : <class 'int'>

#In python every object that is created is given a number that uniquely identifies it 
n=500
m=n
print(id(n))
#60127345
print(id(m))
#60127345

m=600
print(id(m))
#60127371

#####  Variable names in Python can be any length and
# can consist of uppercase and lowercase letters(A-Z,a-z)
# digits(0-9), and the underscore charecter(_)and 
# the first charecter of a variable name cannot be a digit 

#For example, all of the following are valid varible names :

name= "Ram"
Age=30
has_atm=True
print(name, Age , has_atm)

# o/p : Ram 30 True

#  233_filed=False
#  Syntax error

age=1
Age=2
aGe=3
AGE=4
a_g_e=5
_age=6
age_=7
_AGE_=8

print(age, Age, aGe, AGE, a_g_e, _age, age_, _AGE_)
# o/p : 1 2 3 4 5 6 7 8 

numberofcollegegraduates=25000
NUMBEROFCOLLEGEGRADUATES=25000
print(numberofcollegegraduates,NUMBEROFCOLLEGEGRADUATES)
# o/p : 2500 2500

#Camel Case  : numberOfCollegeGraduates : Second and Subsequent words are capitalized
#Pascal Case : NumberOfCollegeGraduates : first word is capitalized
#Snake Case  : number_of_college_graduates : words are superated by underscores






