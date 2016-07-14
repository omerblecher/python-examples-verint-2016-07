#Calculate sum of all tens digits
def tendigitssum(*nums):
    return sum([(n / 10) % 10 for n in nums if type(n) == int])

print tendigitssum(140, 220, 1120)