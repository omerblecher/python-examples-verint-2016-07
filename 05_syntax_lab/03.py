#Sum of digits

from random import randint

#get a number between 1 to 10,000
number = randint(1, 10000)
print "The number is: {}".format(number)

sum = 0

#Loop over the digits
while number > 0:
    sum += number % 10
    number /=10

print "The sum of all digits is {}".format(sum)