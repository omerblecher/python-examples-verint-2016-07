#Append file 1 into the end of file 2
import sys

(src, dst) = sys.argv[1:]

with open(src, "r") as fin: #Open file for reading
    with open(dst, "a+") as fout: #Open file for appending. If the file doesn't exist then create it
        for line in fin:
            fout.write(line) #Copy each line
