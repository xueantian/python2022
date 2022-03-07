
import os
#os.open('/Users/xueatian/Downloads/6770N70.pdf','r')

f=open(os.path.expanduser('/Users/xueatian/Documents/python2022/2/word.txt'))
print(f)
print (os.getcwd())

os.chdir('/Users/xueatian/Documents/')
print (os.getcwd())
os.makedirs('a/b/c')
os.removedirs('a/b/c')
os.remove('a')