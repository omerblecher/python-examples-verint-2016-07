#Summer class

class Summer(object):

    #Constructor
    def __init__(self):
        self._total = 0

    #Add function. Can get one or more integers
    def add(self, *numbers):
        for num in numbers:
            if type(num) == int:
                self._total += num
            else:
                raise ValueError("%s is not an integer!" % (num))

    #Return the total
    def total(self):
        return self._total




s = Summer()
t = Summer()

s.add(10, 20)
t.add(50)
s.add(30)

# should print 60
print s.total()

# should print 50
print t.total()
        