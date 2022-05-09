import re
s='I like study everyday'
print(re.search('.',s).group())

print(re.findall('e',s))
print(re.sub('like','love',s))