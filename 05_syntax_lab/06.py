#lcm
from random import randint

firstNumner = randint(1, 10)

secondNumner = randint(1, 10)

gcd = 0
a = firstNumner
b = secondNumner

#Calculate gcd
while True:
    if(a == b):
        gcd = a
        break;
    elif a > b:
        a -= b
    else:
        b -= a

#Set lcm

lcm = (firstNumner * secondNumner) / gcd

print "The lcm of %d and %d is %d" % (firstNumner, secondNumner,  lcm)

