import re

with open(r"D:\Python_core\python-core-concepts2\regex\textdata.txt",'r') as f:
    contents=f.read()

    for match in re.compile(r'\d\d\d.\d\d\d.\d\d\d\d').findall(contents):
        print(match)
    print()
    for match in re.compile(r'\d\d\d[-,$*]\d\d\d[-*,$]\d\d\d\d').finditer(contents):
        print(match)
    print()
    for match in re.compile(r'[67]\d\d[-*]\d\d\d[-*]\d\d\d\d').finditer(contents):
        print(match)
    print()

    for match in re.compile(r'\d{3}-\d{3}-\d{4}').finditer(contents):
        print(match)

    print(contents[12:24])


    for match in re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*').finditer(contents):
        print(match)
    print()

    for match in re.compile(r'[a-zA-Z0-9.]+@[a-zA-Z]+\.(com|edu)').finditer(contents):
        print(match)
    print()

    for match in re.compile(r'https?://(www\.)?\w+\.\w+').finditer(contents):
        print(match.group(0))
    print()

    


