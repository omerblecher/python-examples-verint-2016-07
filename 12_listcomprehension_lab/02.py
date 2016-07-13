#All three letters permutation

#Generate a list of all lower letters
lowerletters = [chr(index) for index in range(ord('a'),ord('z'))]

#Generate all three letters permutations
threeletters = [a + b + c for a in lowerletters for b in lowerletters for c in lowerletters]

#Print all permutations
print " ".join(threeletters)