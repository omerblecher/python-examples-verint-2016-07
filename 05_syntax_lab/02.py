#Sum of 7 numbers

from random import randint

sum = 0

#Get 7 numbers
for number in range(7):
    sum += randint(1, 100)

print "The sum of the 7 random numbers is {}".format(sum)

# check if the sum is divided by 7
if sum % 7 == 0:
    print "boom"
