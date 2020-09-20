import re

string = 'search inside asdf;   oiupoialskjdf;lwek of 2as41028709_(*&0987-9q7 this text please!'

pattern = re.compile('\W')

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)

print(b)
