import time
from math import ceil
#a=math.cos(30)
#print(a)
b=ceil(8.1)
print(b)

from function1 import caluc
c=caluc(1,2)
print(c)


from urllib import request

a=request.urlopen(url='http://www.baidu.com')
print(a)

import schedule

aa = input('your word:')
def hello2():
    print(aa)

def hello3():


    schedule.every(2).seconds.do(hello2)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__  == '__main__':
    hello3()