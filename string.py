

a = 'hello,world,hello'
print(a.rindex('e'))
print(a.find('l'))
print(a.rfind('l'))
b=a.count('l')
print(b)
c=a.center(40,"*")
print(c)


g=a.replace('hello','nihao')
d=g.split(sep=',')
print(g)
print(d)
for e in d:
    print(e)