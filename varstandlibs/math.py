import math
import logging
logging.basicConfig(level=logging.DEBUG)
a,b=2,4
logging.debug("{:.2f}".format(math.sqrt(b)))
c=(8,3,24,12,7)
for i in c:
    if i%2==0:
        d=math.factorial(i)
    else:
        d=math.factorial(i)
    print(d,end=" ")
logging.debug(" ")
e=5.7839
logging.debug(math.ceil(e))
logging.debug(math.floor(e))
f,g=29,-34
logging.debug(math.copysign(f,g))
logging.debug(math.fabs(e))
h,i=55,32
logging.debug(math.fmod(h,i))
logging.debug(math.frexp(25))
li=[5,33,64,99]
logging.debug(math.fsum(li))
j=3
logging.debug(math.isfinite(j))
k,l=3,4
logging.debug(math.ldexp(k,l))
m=88.3849838
logging.debug(math.trunc(m))
n=7
logging.debug(math.exp(n))
logging.debug(math.expm1(n))
o=0.43
logging.debug(math.asin(o))
p=8
logging.debug(math.degrees(p))
logging.debug(math.erf(p))
logging.debug(math.pi)