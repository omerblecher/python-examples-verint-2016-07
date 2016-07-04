#Reverse

print "Enter some lines and the results will be print backward: \n"

results = ""

while True:
    userInput = raw_input()
    if len(userInput) == 0:
        break
    results = userInput + "\n" + results

#print all lines backward
if len(results) > 0:
    print results
else:
    print "Empty input"
