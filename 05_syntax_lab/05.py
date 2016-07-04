#Divided by 7, 13 and 15
from random import randint 

foundNumber = 0

#find number which is divided by 7, 13 & 15

while True:
    foundNumber = randint(1, 1000000)
    if foundNumber % 7 == 0 and foundNumber % 13 == 0 and foundNumber % 15 == 0:
        break

print "Number between 1 to 1,000,000 which is divided by 7, 13 and 15 is {}".format(foundNumber)
     
