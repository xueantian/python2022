import requests
# get the name of novel
#//div[@class="book-mid-info"]/h2/a/text()
# get the author of the novel
#//p[@class="author"]/a[1]/text()
import requests
import lxml.etree
url='https://www.qidian.com/rank/yuepiao/'
header={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'}

resp=requests.get(url,headers=header)
e=lxml.etree.HTML(resp.text)


names=e.xpath('//div[@class="book-mid-info"]/h2/a/text()')
authors=e.xpath('//p[@class="author"]/a[1]/text()')

#print(names)
#print(authors)
i=0

try:
    while True:
        print('小说名字是：',names[i],'作者是：',authors[i],'\n')
        i+=1
except Exception as e:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for names,authors in zip(names,authors):
    print(names,":",authors)


