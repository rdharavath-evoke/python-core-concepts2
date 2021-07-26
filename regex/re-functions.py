import re
import logging

logging.basicConfig(level=logging.DEBUG)
str="python3 is a good programming language"
r1=re.findall(r"^\w+",str)
logging.info("'^' start of a string and '\w+'alphanumeric ")
logging.debug(r1)

r2=re.findall(r'\s',str)
logging.info("'\s'space charecter")
logging.debug(r2)

r3=re.findall(r'\d',str)
logging.debug(r3)

str="python is looking like fun programming language in 2021"
result=re.match(r'python',str)
if result:
    print("result :",result)
else:
    print("no result :",result)

list1=["hello22","python3","program","version2","2021"]
for str in list1:
    result1=re.match(r"(h\w+)",str)
    if result1:
        print((result1.group()))
    else:
        print(result1)



patterns=['software testing','guru99']
text="python programming is hard"
for pattern in patterns:
    print('looking for "%s" in "%s"->'%(pattern,text),end=" ")
    if re.search(pattern,text):
        print("found a match")
    else:
        print("not found")
