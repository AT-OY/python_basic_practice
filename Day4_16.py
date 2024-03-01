import re


def double(matched):
    value = int(matched.group("value"))
    return str(value * 2)


def twice(matched):
    value = int(matched.group())
    return str(value * 2)


s = "A23G4HFD567"
print(re.sub("(?P<value>\d{1})", double, s))
print(re.sub("(\d{1})", twice, s))
