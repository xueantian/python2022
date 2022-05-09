
import urllib.request
from http import cookiejar


def get_cookie(i):

    url0='http://www.baidu.com'
    url1='https://www.router-switch.com/'
    url2='https://www.google.com'
    url3='https://www.facebook.com'
    url_lib=[url0,url1,url2,url3]

    filename = 'cookie{}.txt'.format(i)
    cookie = cookiejar.MozillaCookieJar(filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    opener.open(url_lib[i])
    cookie.save()
    return filename




def read_cookie(filename):

    cookie=cookiejar.MozillaCookieJar()
    cookie.load(filename)
    print(cookie)

if __name__ == '__main__':
    i = 0
    while i < 4:
        result=get_cookie(i)
        #print(result)
        read_cookie(result)
        i += 1
