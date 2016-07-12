#List of all lower case letters

#Generate a list of all lower letters
lowerletters = [chr(index) for index in range(1,256) if index >= ord('a') and index <= ord('z')]
print " ".join(lowerletters)
