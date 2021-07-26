import re
import logging
from typing import Pattern

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

data="""
Name=Sachin Tendulkar
Age=40
Phone_No=8235792323
landline_No=489-38499
Gender=Male
Gmail=sachinTendulka1980.cricket@gmail.com
profession=cricket
Address=3-101,Rb st. Mumbai,Maharashtra-394852


Name=Pusarla Sindhu
Age=28
Phone_No=9485798363
landline_No=384-38494
Gender=Female
Gmail=sindhuPusarla1995.badminton@gmail.com
profession=Badminton
Address=5-105,VL st. Hyderabad,Telangana-830348

Name=Cristiano Ronaldo
Age=34
Phone_No=9849956733
landline_No=789-30499
Gender=Male
Gmail=CristianoRonaldo@gmail.com
profession=Soccer
Address=8-105,RK st.,paris,Porchugal-394852

"""

pattern=r"Name"
result=re.match(pattern,data)
if data:
    print('Success :',result)
else:
    print('Unsuccess')

pattern=r"[a-zA-Z]\w+=\d{10}"
for phone_no in re.compile(pattern).findall(data):
    logging.debug("  %s",phone_no)


pattern=r"[a-zA-Z]\w*=\d{3}-\d{5}"
for land_no in re.findall(pattern,data):
    logging.debug("  %s",land_no)

pattern=r"[a-zA-Z]\w=\d{3}-\d{5}"
for land_no in re.findall(pattern,data):
    logging.debug("  %s",land_no)
logging.debug("\n")

pattern=r"[a-zA-Z]\w+=[a-zA-Z]\w+\s[a-zA-Z]\w+"
for name in re.findall(pattern,data):
    print(name)