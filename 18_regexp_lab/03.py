import re
import sys
#CSV column replacements


with open(sys.argv[1], "r") as fin:
    for line in fin:
        word = line.strip(' \t\n\r')
        if len(word) > 0 :
            res = re.search(r'^(.+),(.+),(.+)$', word) #Get all the column values
            if res is not None:
                print "%s,%s,%s" % (res.group(2), res.group(1), res.group(3))