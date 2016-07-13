#sum of a list
def mysum(*nums):
    return sum([n for n in nums if type(n) == int])

#multiple of a list
def mymul(*nums):
    list = [n for n in nums if type(n) == int]
    list.extend([1,1])            #Add 1,1 in a case when there is no number
    return reduce(lambda x, y: x*y, list)

#testing
print mysum(20, 30)
print mymul(3,4,5,6)
print mysum(30)
print mymul(54)
print mysum(30, "sd", "sd", 5)
print mymul()
print mysum("sd", "sd")
print mymul("sd", "sd")


