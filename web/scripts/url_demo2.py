import ssl
import urllib.request
import urllib.parse

url='https://39.155.171.87:8443/'
data={'username':'tianxan','password':'@@987128tian','action':'login'}

resp=urllib.request.urlopen(url,data=bytes(urllib.parse.urlencode(data),encoding='utf-8'),context=ssl.CertificateError)

aaa=urllib.request.urlopen()


#html=resp.read().decode('utf-8')

resp=urllib.request.Request(url)
print(resp)