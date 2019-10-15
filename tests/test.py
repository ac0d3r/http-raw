import httpraw

print('='*20, 'raw', '='*20)
raw = '''POST /post HTTP/1.1
Host: httpbin.org
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:45.0) Gecko/20100101 Firefox/45.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 19

key1=val1&key2=val2
'''

# resp is requests Response
resp = httpraw.request(raw=raw)

print(resp.status_code)
print(resp.text[:100])

print('='*20, 'raw2', '='*20)
raw = '''
GET /wx-chevalier/Distributed-Infrastructure-Series/blob/master/%E7%BD%91%E7%BB%9C/HTTP/HTTP%20%E8%AF%B7%E6%B1%82.md HTTP/1.1
Host: github.com
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Referer: http://blog.imipy.com/2019/05/06/read-code-of-requests-module/
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: _ga=GA1.2.883270799.1548518745; tz=Asia%2FShanghai; _octo=GH1.1.1071876509.1548518746; ignored_unsupported_browser_notice=false; _device_id=067fa321a86542359553f0e7975f790e; user_session=FO2WvGH8dejHpc6jbgDehZ4CmTt5xaJRKIh7cTUTk6EaTxOA; __Host-user_session_same_site=FO2WvGH8dejHpc6jbgDehZ4CmTt5xaJRKIh7cTUTk6EaTxOA; logged_in=yes; dotcom_user=Buzz2d0; _gid=GA1.2.1391023066.1557824112; has_recent_activity=1; _gh_sess=cUUrUnJ5OFZ6M1NKaWx2MTlwaG44UHNDeGVTSVJhV1dWcjIyc2w2ZWg4cm91eVhxQmUxdjNTMHdpRzdiYUR5NUZ4Wmo2U01XeFowRGZJazJ6MWVLVmczdkw1LzAxdmRHQ1RNTWRPNzBZUEV1TjFlbkszdGw0RW5jTytZeGFuWHltZ0U4aEJYZ0hNRUlGdmlDTDRuMzY4QmFDU2Z4eE44NDROUEllNXVKZi81MzdRZ2FZVUpVM0VxbXd6UzQ5aG5vMXZLS0VrN0tFdEZGUm5tZjl1QjhGdlhEeXRXbnlNd3Q4dzRJazFXZzZJazZaalBiOE12SXJVSnZPZVhrckN1cnI2blYyQlBJamFHM2UwUWU5ZHBRWTFqT1JYQksyTUZ2Z2Fqd2lUQUR1RXFwNDhiZll0YTkxUDRJU2VzL01PK0x4TTNOMEhNNTJDVnZjMWE4NnJ4QXl3S1dVRkRWbHVIWlJ6UWRKU0gvbDM4U2xnYlU4WWE1WEVmc0JDUnNncXp3LS1sVS9CM0ZYb2JkbnVnWm44VWpJb09RPT0%3D--d0777dd625982717f863c601ea4a8722d4e39076
If-None-Match: W/"d4f55158061d133b35bc03801f54df6f"'''

proxy = {
    'socks5': '127.0.0.1:1086'
}

resp = httpraw.request(raw=raw, ssl=True, timeout=5, verify=True, proxy=proxy)
print(resp.status_code)
print(resp.text[:100])


# proxy
print('='*20, 'raw proxy', '='*20)
proxy = {
    'socks5': '127.0.0.1:1086'
}
raw = '''GET / HTTP/1.1
Host: www.google.com
Connection: close
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: xxx
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
X-Client-Data: CIe2yQEIorbJAQjBtskBCKmdygEIqKPKAQjUpMoBCLGnygEI6KfKAQjiqMoBCPCpygEIr6zKAQ==
Referer: https://www.google.com/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
'''
resp = httpraw.request(raw=raw, proxy=proxy, ssl=True, verify=True)
print(resp.status_code)
print(resp.text[:100])

print('='*20, 'Httpraw proxy', '='*20)
raw = '''GET / HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:45.0) Gecko/20100101 Firefox/45.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Content-Type: application/x-www-form-urlencoded'''
h = httpraw.Httpraw(raw)
h.proxy = {'socks5': '127.0.0.1:1086'}
h.timeout = 5
h.ssl = True
h.verify = True
resp = h.request()
print(resp.status_code)
print(resp.text[:100])

# API Post
print('='*20, 'API Post', '='*20)
url = 'http://httpbin.org/post'
headers = '''
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:45.0) Gecko/20100101 Firefox/45.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Content-Type: application/x-www-form-urlencoded
'''
data = 'key1=val1&key2=val2'
resp = httpraw.post(url, headers=headers, data=data)
print(resp.status_code)
print(resp.text[:100])


# API Get
print('='*20, 'API Get proxy', '='*20)
proxy = {
    'socks5': '127.0.0.1:1086'
}
url = 'http://www.google.com/'
resp = httpraw.get(url, proxy=proxy)
print(resp.status_code)
print(resp.text[:100])
