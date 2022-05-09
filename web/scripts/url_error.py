

import urllib.request
import urllib.error

url='https://www.baidu.com/1/2'
try:
    resp=urllib.request.urlopen(url)
except urllib.error.HTTPError as e:
    print('reason:',e.reason)
    print('code:',e.code)
    print('header:',e.headers)