import os

with open('1.txt','a',encoding='utf-8') as file:

    file.write('hello David!!')
    file.write('\n')
    file.close()
with open('1.txt','r',encoding='utf-8') as rfile:
    word=rfile.read()
    print(word)
    rfile.close()



