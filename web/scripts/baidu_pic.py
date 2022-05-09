import requests
import re

url='https://so.5tu.cn/pic/gaoqingmeinvtuku.html'
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'}

resp=requests.get(url,headers=headers)
resp.encoding='utf-8'
#print(resp.text)

link=re.findall('img src="(http://.*.jpg)',resp.text)
i=0
for item in link:
    print(item)
    pic=requests.get(item,headers=headers)
    with open ('pic/pic{}.jpg'.format(i),'wb') as file:
        file.write(pic.content)
    print('已下载图片{}'.format(i))
    i += 1

print('所有图片下载完毕')


