#All three letters permutation

#Generate a list of all lower letters
lowerletters = [chr(index) for index in range(1,256) if index >= ord('a') and index <= ord('z')]

#Generate all three letters permutations
threeletters = [a + b + c for a in lowerletters for b in lowerletters for c in lowerletters]

#Print all permutations
print " ".join(threeletters)