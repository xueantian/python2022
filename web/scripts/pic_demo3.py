import requests
import re
from lxml import etree

url='https://www.istockphoto.com/jp/search/search-by-asset?affiliateredirect=true&assetid=1329622588&assettype=image&utm_campaign=category_photos_top&utm_content=https%3A%2F%2Funsplash.com%2Fimages%2Ffeelings%2Fbeautiful&utm_medium=affiliate&utm_source=unsplash&utm_term=beautiful%3A%3A%3A'
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'}
resp=requests.get(url,headers=headers)
resp.encoding='utf-8'
print(resp.text)



#link=re.findall('content=\"(https://images.unsplash.*?jpg)',resp.text)

link=re.findall('(https://media.istockphoto.*?=)',resp.text)
print(link)
lst=[]

i=130
for item in link:
    print(item)
    pic = requests.get(item, headers=headers)
    with open('pic/pic{}.jpg'.format(i), 'wb') as file:
        file.write(pic.content)
    print('已下载图片{}'.format(i))
    i += 1

print('所有图片下载完毕')





