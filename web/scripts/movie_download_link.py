
import requests
import re
import csv
import codecs


url='https://www.dytt8.net/html/gndy/jddy/20160320/50523.html' # IMDB评分8分左右影片500多部
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'}
resp=requests.get(url)
resp.encoding='gb2312'
#print(resp.text)

obj1=re.compile(r"<p><strong>.*?<a href=\"(?P<page_link>https://.*?)\">",re.S)

result1=obj1.finditer(resp.text)

obj2=re.compile(r"href=\"(?P<download_link>magnet:.*?)\"><strong><font",re.S)
obj3=re.compile(r"<title>(?P<movie_name>.*?)</title>",re.S)

download_links=[]
movie_names=[]
i=0
lst=[]
for it in result1:
    url2=it.group('page_link')
    print(url2)
    resp2=requests.get(url2,headers=headers)
    resp2.encoding = 'gb2312'
    #print(resp2.text)
    result2 = obj2.finditer(resp2.text)
    result3=obj3.finditer(resp2.text)
    for itt in result2:
        download_links.append(itt.group('download_link'))
        #print(download_links)
    for ittt in result3:
        movie_names.append(ittt.group('movie_name'))
        #print(movie_names)

    final_list=dict(zip(movie_names,download_links))



    i+=1
    print('第 {} 个电影的下载地址'.format(i))
    print(movie_names)
    print(download_links)
    if i == 2:
        break

lst.append(movie_names)
lst.append(download_links)

print(lst)
with open('movie_download_link1.txt', 'a') as file:
    a=0
    for item in movie_names:

        file.write(str(item)+'\t'+'|'+'\t'+download_links[0]+'\n')
        a+=1
    file.close()








