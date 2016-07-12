#host to ip address
import sys


addresses = {}

# create a set of unique computer name from argv
# (excluding program name)
hostnames = set(sys.argv[1:])

#Read host file and save the host & I.P address in the dictionary
with open("hosts", "r") as fin:
    for line in fin:
        hostaddress = line.strip('\n').split('=')
        (host, address) = hostaddress
        addresses[host] = address

#Go over the given names in the argument line and print the I.P address
for name in hostnames:
    if name in addresses:
        print "The I.P. address of %s is %s" % (name, addresses[name])
    else:
        print "%s doesn't exist in the hosts file" % (name)

