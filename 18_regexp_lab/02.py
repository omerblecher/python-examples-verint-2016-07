import re

#To Camel case
def toCamelCase(text):
    allWords = re.split(r'_', text)
    first = allWords[0]
    return first + ''.join([word.title() for word in allWords[1:]])

#From camel case
def fromCamelCase(text):
    return re.sub(r'[A-Z]',
        lambda m: '_' + m.group(0).lower()
        , text)


print toCamelCase('no_more_shall_we_part')
print  fromCamelCase('noMoreShallWePart')
