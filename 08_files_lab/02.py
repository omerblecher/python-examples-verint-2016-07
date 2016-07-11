#Write two files line by line into a third file
import sys
import itertools 

(firstSource, secondSource, dst) = sys.argv[1:]

with open(firstSource, "r") as finFirst: # Open first file for reading
    with open(secondSource, "r") as finSecond: # Open second file for reading
        with open(dst, "w+") as fout: # Open file only for writing. Truncate it if needed
            for step in itertools.izip_longest(finFirst, finSecond): #Get tuple from two files
                for item in step:
                    if item is not None: #Write it to the file only if it is not none
                        fout.write(item)