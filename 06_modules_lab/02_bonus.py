#sum exercise bonus - check parameters

import sys



if (len(sys.argv) < 3):
    print "You need to set 2 integer numbers as parameters to the script"
elif not(sys.argv[1].isdigit()) and not(sys.argv[1].startswith('-') and sys.argv[1][1:].isdigit()): # Validate that argv[1] is positive or negative integer
    print "{} is not a valid integer".format(sys.argv[1])
elif not(sys.argv[2].isdigit()) and not(sys.argv[2].startswith('-') and sys.argv[2][1:].isdigit()): # Validate that argv[2] is positive or negative integer
    print "{} is not a valid integer".format(sys.argv[2])
else:
    first = int(sys.argv[1])
    second = int(sys.argv[2])
    
  

    print "%d + %d = %d" %(first, second, first + second)
