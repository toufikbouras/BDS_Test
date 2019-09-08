
# coding: utf-8

import requests

# the response body of the request sent to this url = 'https://httpbin.org/anything' 
def get_req_body(msg='welcomeuser' , isadmin = '1'):
    
    url = 'https://httpbin.org/anything'
    myobj = {'msg': msg, 'isadmin': isadmin}
    x = requests.post(url, data = myobj)

    print(x.text)


# the response headers of the request sent to this url = 'https://httpbin.org/anything' as a mobile user 

def get_mobreq_headers(msg='welcomeuser' , isadmin = '1'):

    url = 'https://httpbin.org/anything'
    myobj = {'msg': msg, 'isadmin': isadmin}
    headers_mobile = { 'User-Agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 \
                      (KHTML, like Gecko) Version/9.0 Mobile/13B137 Safari/601.1'}
    x = requests.post(url, data = myobj, headers=headers_mobile)
    print(x.headers)

get_req_body()
get_mobreq_headers()
