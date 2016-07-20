#Widget

class Widget(object):
    


    #Constructor
    def __init__(self, name):
        self._name = name
        self._dependDict = {}
        self._isBuilt = False
        self._index = 0   #Index to keep on the inserting order


    #Check if Widget object is in the dependencies list
    def _isDepend(self, name):
        isDepend = False

        for _, val in self._dependDict.items():
            if val._name == name or val._isDepend(name):
                isDepend = True
                break
        return isDepend

    #Check circular dependencies
    def _isCircular(self, widgetObj):
        return widgetObj._isDepend(self._name)

    #Add dependencies
    def add_dependency(self, *widgetObjLis):
        for obj in widgetObjLis:
            if not self._isCircular(obj):   #Add only if there is no circular dependency
                self._dependDict[self._index] = obj
                self._index += 1
            else:
                raise Exception("Circular dependencies %s depends on %s" % (obj._name, self._name))


    #Build all widgets
    def build(self):
        self._isBuilt = True
        for _, val in self._dependDict.items():
            if not val._isBuilt: #Build only objects that haven't been built yet
                val.build()
                print val._name



luke    = Widget("Luke")
hansolo = Widget("Han Solo")
leia    = Widget("Leia")
yoda    = Widget("Yoda")
padme   = Widget("Padme Amidala")
anakin  = Widget("Anakin Skywalker")
obi     = Widget("Obi-Wan")
darth   = Widget("Darth Vader")
_all    = Widget("All")


luke.add_dependency(hansolo, leia, yoda)
leia.add_dependency(padme, anakin)
obi.add_dependency(yoda)
darth.add_dependency(anakin)

_all.add_dependency(luke, hansolo, leia, yoda, padme, anakin, obi, darth)
_all.build()
     



  

