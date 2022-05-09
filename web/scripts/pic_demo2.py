import requests
import re
from lxml import etree

url='https://www.jj20.com/bz/nxxz/nxmt/256949.html'
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'}
resp=requests.get(url,headers=headers)
resp.encoding='utf-8'
#print(resp.text)

link=re.findall('img loadsrc=\"(.*.jpg)',resp.text)
#print(link)
lst=[]
i=112
for item in link:
    lst.append('https:' + item)
    print(lst[i-112])
    pic = requests.get(lst[i-112], headers=headers)
    with open('pic{}.jpg'.format(i), 'wb') as file:
        file.write(pic.content)
    print('已下载图片{}'.format(i))
    i += 1


print('所有图片下载完毕')



