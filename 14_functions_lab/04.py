#Longer than

def longer_than(minLength, *words):
    return [word for word in words if len(word) > minLength]

print longer_than(3, 'hit', 'me', 'baby', 'one', 'more', 'time')
