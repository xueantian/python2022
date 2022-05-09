
import requests

url='https://img1.bdstatic.com/static/searchdetail/img/logo-2X_2dd9a28.png'
url1='https://img1.baidu.com/it/u=3019447217,3540674239&fm=253&fmt=auto&app=138&f=JPEG?w=800&h=500'
resp=requests.get(url1)
with open('pic1.png','wb') as file:
    file.write(resp.content)
