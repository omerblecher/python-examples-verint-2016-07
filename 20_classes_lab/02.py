#MyCounter class

class MyCounter(object):
    
    #Initialize static counter
    count = 0

    #Constructor
    def __init__(self):
        MyCounter.count += 1


for _ in range(10):
     c1 = MyCounter()

# should print 10
print MyCounter.count

