#Guessing number

from random import randint

number = randint(1, 100)

while True:
    guess = int(raw_input("Guess a number: "))
    
    #check if it's the correct number
    if number == guess:
        print "Correct!"
        break

    firstCompare = guess
    secondCompare = number

    #get a random number
    mistake = randint(1, 100)

    #if the number is divided by 19, then we print wrong message
    if mistake % 19 == 0:
        firstCompare = number
        secondCompare = guess

    #Print messages
    if firstCompare > secondCompare:
        print "Too big"
    else:
        print "Too small"
