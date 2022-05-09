import requests
from bs4 import BeautifulSoup

url='https://world.taobao.com/'
headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'}

resp=requests.get(url,headers=headers)
#print(resp.text)

bs=BeautifulSoup(resp.text,'lxml')
a_list=bs.find_all('a')
for a in a_list:
    url2=a.get('href')
    if url2.startswith('http') or url2.startswith('https'):
        with open('taobao_link.txt','a') as file:
            file.write(url2)
            file.write('\n')

    else:
        continue