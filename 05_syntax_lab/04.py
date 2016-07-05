#Reverse

print "Enter some lines and the results will be print backward: \n"

results = []


while True:
    userInput = raw_input()
    if len(userInput) == 0:
        break
    results.append(userInput)
  

#print all lines backward
if len(results) > 0:
    for i in range(len(results)):
        print results[len(results) - i - 1]

else:
    print "Empty input"
