import logging
logging.basicConfig(level=logging.DEBUG)
list_=[0,1,2,3,4,5,6,7,8,9]
logging.info(list_)
list_compr=[x*2 for x in range(0,10)]
logging.debug(list_compr)

lambda_list=list(map(lambda x : x*2,list_))
logging.debug(lambda_list)

adding=(lambda x:x+2)(2)
logging.debug(adding)

add_one=lambda x: x+1
logging.debug(add_one(30))

full_name=lambda first,last : f'Full name:{first.title()} {last.title()}'
logging.debug(full_name('guido', 'van rossum'))
high_ord_func=lambda x :x//2
print(high_ord_func(2))
div_zero=lambda x:x/0
print(div_zero)
logging.debug((lambda x: (x%2 and 'odd' or 'even'))(10))
logging.debug((lambda x,y,z=5: x+y+z)(1,2))