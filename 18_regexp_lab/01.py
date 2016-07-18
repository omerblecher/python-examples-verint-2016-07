#Definition file

import re
import sys

(defFile, userkey) = sys.argv[1:]
defDict = {}

#Insert value into the dictionary
with open(defFile, "r") as fin:
    for line in fin:
        word = line.strip(' \t\n\r')
        if len(word) > 0 and not word.startswith('#'):
            (key, value) = re.split(r'[=]', line)
            defDict[key.strip(' \t\n\r')] = value.strip(' \t\n\r')

#Print the value that mact
if userkey in defDict.keys():
    print defDict[userkey]
else:
    print "%s is not in the definition file" % (userkey)
