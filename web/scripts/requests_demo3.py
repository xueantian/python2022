import requests
url='https://image.baidu.com/search/acjson?tn=resultjson_com&logid=10320671839663019761&ipn=rj&ct=201326592&is=&fp=result&fr=&word=%E7%BE%8E%E5%A5%B3&cg=girl&queryWord=%E7%BE%8E%E5%A5%B3&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn=240&rn=30&gsm=f0&1647390608924='
url1='https://www.baidu.com'
resp=requests.get(url1)
resp.encoding='utf-8'
content1=resp.json()

print(content1)