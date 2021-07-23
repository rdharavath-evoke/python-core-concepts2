import random
import logging

logging.basicConfig(level=logging.DEBUG)
list1=[1,2,3,4,5,6,7,8,9]
logging.debug(random.choice(list1))
string="hello python"
logging.debug(random.choice(string))