import re

def data(str):
    pattern=re.compile(r'^a-zA-Z0-9.').search(str)
    
    return not bool(pattern)

print(data('ABCDaafj8494af'))

line="Cats are smarter than dogs"
pattern=re.match(r'Cats',line)
if pattern:
    print("result: ",pattern)
else:
    print("none")


line='python'
pattern=re.match(r'([Pp]ython(,)?)+',line)
print(pattern)