class player(object):
    def __init__(self, name, identity):
        if not(identity == "X" or identity == "O"):
            raise ValueError("Identify must be X or O, not %s!" % (identity))
        self._name = name
        self._identity = identity

    def GetName(self):
        return self._name

    def GetIdentity(self):
        return self._identity