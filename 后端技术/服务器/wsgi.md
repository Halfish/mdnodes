要讲清楚 WSGI 是啥，得先把相关的术语梳理清楚
1. Web Client/Server:
    - 网页服务器，如 Gunicorn/Apache/Nginx/Lighttpd 等
    - 接收客户端（一般是浏览器、手机客户端等）的 HTTP/HTTPS request 请求，返回对应的资源。
2. Web Application
    - 绑定一个端口，提供某种服务，和 web server 通信
3. Web Framework
    - 实现上面 web application 的框架，如 flask，tornado，djongo 等

定义清楚上面几个术语以后，就可以解释 WSGI 的概念了。

WSGI， Web Server Gateway Interface，网页服务网关接口，是一个沟通 web server 和 web application 的统一接口和协议。现在的 web server 和 web application 都是遵从 WSGI 去开发和对接的。

具体的 WSGI 规范内容可以参考 python 社区制定的标准：
- [PEP-0333](https://www.python.org/dev/peps/pep-0333/)
- [PEP-3333](https://www.python.org/dev/peps/pep-3333/)

如下图：
![wsgi](https://bs-uploads.toptal.io/blackfish-uploads/uploaded_file/file/192775/image-1582505123212-d71812e36fd836399c48a034f9e70128.png)

## Application Interface
```
def application(environ, start_response):
    start_response(status='200 OK', headers=[('Content-type', 'text/plain')])
    return [b'Hello World!\n']
```

## Server Interface
```
def write(chunk):
    pass
    
def send_status(status):
    pass
    
def send_headers(headers):
    pass
    
def start_response(status, headers):
    send_status(status)
    send_headers(headers)
    return write

response = application(environ, start_response)
try:
    for chunk in response:
        write(chunk)
finally:
    if hasattr(response, 'close'):
        response.close()
```
