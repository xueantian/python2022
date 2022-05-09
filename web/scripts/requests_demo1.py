import requests

url='https://www.baidu.com'
resp=requests.get(url)
cookie=resp.cookies
a=resp.text
print(resp)
print(cookie)
print(a)

