#Files exercise, find all files that are greater than 1 MB
import os
import sys
MEGA = 1024 * 1024

rootPath = "."
minSize = MEGA
if len(sys.argv) > 1:
    #Set the root path from command line arguments
    rootPath = sys.argv[1]
if len(sys.argv) > 2:
    #Set the minimum file size to delete from command line arguments
    minSize = int(sys.argv[2])

print "Looking recursively for all files under %s and looking for files that their size is greater than %d bytes" % (rootPath, minSize)

for root, dirs, files in os.walk(rootPath):
    for name in files:
        fullPath = root + "\\" + name
        statinfo = os.stat(fullPath)
        if statinfo.st_size >= minSize:
            #Print the file
            print "File: %s, Size %d bytes" % (name, statinfo.st_size) 
            #Ask the user whether to delete the file or not
            toDelete = raw_input("Do you want to delete this file y/n?")
            if toDelete == "y" or toDelete == "Y":
                os.remove(fullPath)
        
