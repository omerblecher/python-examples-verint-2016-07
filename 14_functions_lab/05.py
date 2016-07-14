#Create dictionary from a list of arguments
from collections import defaultdict

def groupby(func, *params):
    groupbydict = defaultdict(list)
    [groupbydict[func(word)].append(word) for word in params]
    return groupbydict

print groupby(lambda(s): s[0], 'hello', 'hi', 'help', 'bye', 'here')
