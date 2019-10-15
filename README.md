# http-raw
[![PyPI version](https://img.shields.io/badge/pypi-0.2.1-green.svg)](https://pypi.org/project/http-raw/)
[![Python version](https://img.shields.io/badge/python-3-orange.svg)]()

A library for better processing of raw data✌️

## Install

```bash
pip install http-raw
```

## Use

```python
import httpraw

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
print(resp.text)

proxy = {
    'socks5': '127.0.0.1:1086'
}
resp = httpraw.request(raw=raw, proxy=proxy, timeout=5, ssl=True, verify=True)

# use api
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
```

## Dev

```bash
pipenv install --dev
```
