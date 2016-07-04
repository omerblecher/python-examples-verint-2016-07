#Max Number
import sys

print "Enter 10 numbers: "
print " "

maxNumber = -sys.maxint

# loop for the next 10 numbers
for n in range(1, 11):
    sys.stdout.write("Number {}: ".format(n))
    number = int(raw_input())
    if number > maxNumber : 
        maxNumber = number

#print the results
print "The biggest number is {}".format(maxNumber)