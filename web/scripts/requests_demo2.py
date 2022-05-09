
import requests
url='https://www.baidu.com'
params={'q':'田学安'}
resp=requests.get(url)
resp.encoding='utf-8'
result=resp.text
print(result)