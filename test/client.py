import urllib.request
import urllib.parse


url='http://176.122.146.160:8000/impweb/sign_up/'
data={
    'username':'ijjkenrf',
    'password':'jiklnh',
    'email':'asdfasdfjkjkn@lkl.com',
    'facebook':'lzsjkn'
}
endata=urllib.parse.urlencode(data).encode(encoding='UTF8')


req = urllib.request.Request(url, endata)
f=urllib.request.urlopen(req)

s=f.read().decode('utf-8')
print(s)
