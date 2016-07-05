#Max Number

print "Enter 10 numbers: "
print " "


# loop for the next 10 numbers
for n in range(1, 11):

    number = int(raw_input("Number {}: ".format(n)))
    if n == 1 or number > maxNumber : 
        maxNumber = number

#print the results
print "The biggest number is {}".format(maxNumber)