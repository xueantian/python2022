

dicta = {1:1,2:2, 3:3,'c':4}
dictb = dict(name = 1, book = 2)
print(dicta)
print(dictb)

print(dicta[1])
print(dictb.get('name'))
keys =list(dictb.keys())
values=list(dictb.values())
items=dictb.items()
print(keys,values)
print(list(items))

for i in dictb:
    print(i,dictb[i],dictb.get(i))