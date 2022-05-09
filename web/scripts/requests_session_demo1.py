import  requests
url='https://www.baidu.com'

resp1=requests.session()
resp=resp1.get(url)
print(resp.text)

