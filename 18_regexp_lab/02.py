import re

#To Camel case
def toCamelCase(text):
    return re.sub(r'_[a-z]',
        lambda m: m.group(0)[1].upper()
        , text)

#From camel case
def fromCamelCase(text):
    return re.sub(r'[A-Z]',
        lambda m: '_' + m.group(0).lower()
        , text)


print toCamelCase('no_more_shall_we_part')
print  fromCamelCase('noMoreShallWePart')
