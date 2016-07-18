#Definition file

import re
import sys

(defFile, key) = sys.argv[1:]
defDict = {}

#Insert value into the dictionary
with open(defFile, "r") as fin:
    for line in fin:
        word = line.strip(' \t\n\r')
        if not word.startswith('#'):
            keyvalue = re.split(r'[=]', line)
            defDict[keyvalue[0].strip(' \t\n\r')] = keyvalue[1].strip(' \t\n\r')

#Print the value that mact
if key in defDict.keys():
    print defDict[key]
else:
    print "%s is not in the definition file" % (key)
