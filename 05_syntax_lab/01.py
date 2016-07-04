#Max Number

print "Enter 10 numbers: "
print " "

print "Number 1: "
max = int(raw_input())

# loop for the next 10 numbers
for n in range(2, 11):
    print "Number {}:".format(n)
    number = int(raw_input())
    if number > max : 
        max = number

#print the results
print "The biggest number is {}".format(max)