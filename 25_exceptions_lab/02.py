#Number of lines in file
import sys

src = sys.argv[1]

try:
    with open(src, "r") as fin:
        print sum(1 for line in fin)
except Exception as e:
    #Print an error if file not found
    print "Sorry, file %s not found" % (src)
