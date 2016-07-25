#SQRT - Raise exception if object is not a number
import math

def sqrt(input):

    #Convert to int. The caller should catch the exception
    number = int(input)
    
    #Check if greater than 0
    if number < 0:
        raise ValueError("Expected parameter >= 0, Got: %d" % number)
    return math.sqrt(number)

#Infinite loop till the user quit
while True:
    input = raw_input("Please enter a number, or q to quit: ")
    
    #break means the 
    if input.startswith("q"):
        print "Bye bye"
        break

    try:
        print sqrt(input)
    except Exception as e:
        print "Bad input. Details: ", e
