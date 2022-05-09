
import urllib.parse
import urllib.request
kw={'word':'david田'}
result=urllib.parse.urlencode(kw)
print(result)
back=urllib.parse.unquote(result)
print(back)

webopen=urllib.request.urlopen('http://www.baidu.com')
result=webopen.read().decode('utf-8')
print(result)
