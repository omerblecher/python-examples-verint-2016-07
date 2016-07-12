#anagrams
import sys
from collections import defaultdict

#Read the file name
fileName = sys.argv[1]

#Initialize default dictionary of list. 
anagramDict = defaultdict(list)

with open(fileName, "r") as fin:
    for line in fin:
        word = line.strip('\n') #Remove the end line character
        key = ''.join(sorted(word.lower())) #generate a key of sorted lower case of the word
        anagramDict[key].append(word) #Add the word to the list of the corresponding key

#Print each list in the dictionary, separate with space between each word
for _, v in anagramDict.items():
    print " ".join(v)
