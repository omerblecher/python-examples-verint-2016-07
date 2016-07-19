import re
import sys
#CSV column replacements


with open(sys.argv[1], "r") as fin:
    for line in fin:
        word = line.strip(' \t\n\r')
        if len(word) > 0 :

            columns = re.findall(r'(.+?)(?:,|$)', word) #Get all the column values
            temp = columns[0]
            columns[0] = columns[1]
            columns[1] = temp #Swap
            print ','.join(columns)