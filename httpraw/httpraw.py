# coding: utf-8
import socket
from typing import Dict, List, Optional, Tuple
from urllib.parse import urljoin, urlparse

import requests
import socks
from requests import Response

__all__ = [
    'Httpraw',
    'request',
    'get',
    'options',
    'head',
    'post',
    'put',
    'patch',
    'delete'
]


class HttpRawException(Exception):
    '''Httpraw Exception'''
    pass


class Httpraw:
    def __init__(self,
                 raw: str = '',
                 proxy: Dict[str, str] = {},
                 timeout: int = 0,
                 ssl: bool = False,
                 verify: bool = False):
        self.raw = raw
        self.proxy = proxy
        self.timeout = timeout
        self.ssl = ssl
        self.verify = verify

    def request(self) -> Response:
        request_line, header_lines, body_lines = _parse_raw(self.raw)
        method, path, _protocol = _get_request_info(request_line)
        headers = _get_headers(header_lines)
        body = _get_body(body_lines, headers.get('Content-Type', ''))
        url = self.__get_url(headers, path)

        params = {}
        proxy = self._proxy()
        if self.timeout:
            params['timeout'] = self.timeout
        if self.ssl and self.verify:
            params['verify'] = self.verify
        if body:
            params['data'] = body
        if proxy:
            params['proxy'] = proxy
        return requests.request(method, url, headers=headers, **params)

    def __get_url(self, headers: Dict[str, str], path: str) -> str:
        scheme = "http"
        port = 80
        if self.ssl:
            scheme = 'https'
        host = headers.get('Host', '')
        if ':' in host:
            host, port = host.split(':')
        if int(port) == 80:
            return urljoin(f'{scheme}://{host}', path)
        return urljoin(f'{scheme}://{host}:{port}', path)

    def _proxy(self) -> Dict[str, str]:
        '''处理 socks5，http 和 https 都丢给 requests 自带的去处理
        '''
        if not self.proxy:
            return self.proxy

        proxy_info = self.proxy.get('socks5', '')
        if proxy_info:
            if ":" in proxy_info:
                addr, port = proxy_info.split(':')
                socks.set_default_proxy(
                    proxy_type=socks.PROXY_TYPE_SOCKS5,
                    addr=addr,
                    port=int(port))
                socket.socket = socks.socksocket
            del self.proxy['socks5']
        return self.proxy


class ApiHttpraw(Httpraw):
    def __init__(self,
                 url: str,
                 data=None,
                 headers=None,
                 proxy: Dict[str, str] = {},
                 timeout: int = 0,
                 verify: bool = False):
        '''
        :param data: type can Dict or str
        :param headers: type can Dict or str
        '''
        self.url = url
        self.__headers = headers
        self.__data = data
        self.proxy = proxy
        self.timeout = timeout
        self.verify = verify

    def __parse_headers_data(self):
        headers = {}
        data = ''
        if self.__headers:
            if isinstance(self.__headers, str):
                header_lines = self.__headers.rstrip().split('\n')
                headers = _get_headers(header_lines)
            elif isinstance(self.__headers, Dict):
                headers = self.__headers
        if self.__data:
            if isinstance(self.__data, str):
                body_lines = self.__data.rstrip().split('\n')
                data = _get_body(
                    body_lines, headers.get('Content-Type', ''))
            elif isinstance(self.__data, Dict):
                data = self.__data
        return headers, data

    def request(self, method):
        params = {}
        proxy = self._proxy()
        headers, data = self.__parse_headers_data()
        if headers:
            params['headers'] = headers
        if data:
            params['data'] = data
        if self.timeout:
            params['timeout'] = self.timeout
        if self.verify:
            params['verify'] = self.verify
        if proxy:
            params['proxy'] = proxy

        return requests.request(method.upper(), self.url, **params)


def _parse_raw(raw: str):
    header_lines = []
    body_lines = []
    raw_lines = raw.lstrip().split('\n')
    request_line = raw_lines[0].strip()
    try:
        header_end = raw_lines.index('')
    except:
        header_end = len(raw_lines)
    for line in raw_lines[1:header_end]:
        header_lines.append(line.strip())
    if header_end != len(raw_lines):
        body_lines = raw_lines[header_end+1:]
    return request_line, header_lines, body_lines


def _get_request_info(request_line: List) -> Tuple:
    try:
        method, path, protocol = request_line.split(" ")
    except:
        raise HttpRawException('Protocol format error')
    return method.upper(), path, protocol


def _get_headers(header_lines: List) -> Dict[str, str]:
    headers = {}
    for line in header_lines:
        line = line.strip()
        if ': ' in line:
            k, v = line.split(': ')
            headers[k.strip()] = v.strip()
    return headers


def _get_body(body_lines: List, content_type: str) -> str:
    if 'multipart/form-data' in content_type:
        return '\r\n'.join(body_lines)
    elif ('application/json' in content_type or 'application/x-www-form-urlencoded' in content_type):
        body = ''
        for line in body_lines:
            if line != '':
                body += line.strip()
        return body
    elif 'text/xml' in content_type:
        return '\n   '.join(body_lines)
    else:
        return ''


def request(raw, **kwargs):
    return Httpraw(raw, **kwargs).request()


def get(url, **kwargs):
    return ApiHttpraw(url, **kwargs).request('get')


def options(url, **kwargs):
    return ApiHttpraw(url, **kwargs).request('options')


def head(url, **kwargs):
    return ApiHttpraw(url, **kwargs).request('head')


def post(url, data=None, **kwargs):
    return ApiHttpraw(url, data=data, **kwargs).request('post')


def put(url, data=None, **kwargs):
    return ApiHttpraw(url, data=data, **kwargs).request('put')


def patch(url, data=None, **kwargs):
    return ApiHttpraw(url, data=data, **kwargs).request('patch')


def delete(url, **kwargs):
    return ApiHttpraw(url, **kwargs).request('delete')
