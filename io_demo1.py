import os

file=open('word.txt','r')
print(file.read())

i=1
while i <5:
    filew=open('word.txt','a')
    a=input('input a new line,please:')
    filew.write(a)
    filew.flush()


    filer=open('word.txt','r')
    print(filer.read())


    i+=1

filer.close()


