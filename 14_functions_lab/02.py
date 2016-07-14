#Validate parameters

def validate(text, integerNumber):
    if type(text) != str : raise Exception("text is not a string")
    if type(integerNumber) != int : raise Exception("integerNumber is not an integer")
    print "Text %s, Integer %d" % (text, integerNumber)

validate("hello", 5)