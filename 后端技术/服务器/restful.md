# Restful 接口

| 参数传递方式 | 适用请求类型  | 请求接口                                      | Content-Type                        | 处理数据                        |
|--------------|---------------|-----------------------------------------------|-------------------------------------|---------------------------------|
| URL参数      | GET、DELETE   | `requests.get(url, params={"age": 13})`       | N/A                                 | `request.args`                  |
| JSON数据     | POST、PUT     | `requests.post(url, json={"age": 13})`        | `application/json`                  | `request.json`                  |
| 表单参数     | POST、PUT     | `requests.post(url, data={"age": 13})`        | `application/x-www-form-urlencoded` | `request.form`                  |
| 二进制数据   | POST、PUT     | `requests.post(url, data=b'\x01\xa2', headers=headers)` | `application/octet-stream`               | `request.data`                 |
| 上传文件     | POST、PUT     | `requests.post(url, files=files)`             | `multipart/form-data`               | `request.files`                 |


## 1. Flask 处理接口请求

在 Flask 中，可以通过以下几种方式来获取 POST 请求传递的数据：

### 1.1 URL参数 request.args

request.args 主要用于获取 URL 中的查询参数。

```python
from flask import request

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    return f'Search query: {query}'
```

### 1.2 JSON数据 request.json

用于获取 JSON 数据，数据格式为 `application/json`

返回的数据是解析后的 Python 字典。

```python
from flask import request

@app.route('/json', methods=['POST'])
def get_json():
    data = request.json
    name = data.get('name')
    age = data.get('age')
    return f'Name: {name}, Age: {age}'
```

### 1.3 表单数据 request.form

用于获取表单数据，数据格式为 `application/x-www-form-urlencoded`。

你可以使用键值对的形式访问表单中的数据。

```python
from flask import request

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    return f'Username: {username}, Password: {password}'
```

### 1.4 二进制数据 request.data

用于获取原始的二进制请求体数据。

适用于数据格式不是 form 或 json，如自定义数据格式。

```python
from flask import request

@app.route('/data', methods=['POST'])
def get_data():
    raw_data = request.data
    return f'Raw data: {raw_data}'
```

### 1.5 上传文件 request.files

用于获取上传的文件数据。

可以使用键值对的形式访问上传的文件。

```python
from flask import request

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save(f'./uploads/{file.filename}')
    return f'File {file.filename} uploaded successfully'
```


## 2. requests 库请求接口

### 2.1 发送 URL 参数

```python
import requests

url = 'https://api.example.com/data'
params = {'key1': 'value1', 'key2': 'value2'}

# 适合 GET、DELETE 请求
response = requests.get(url, params=params)
print(response.url)
print(response.text)
```

请求 URL 会自动附加查询参数，如 `https://api.example.com/data?key1=value1&key2=value2`。


### 2.2 发送 JSON 数据

```python
import requests

url = 'https://api.example.com/data'
payload = {'key1': 'value1', 'key2': 'value2'}

# 适合 POST、PUT、PATCH 请求
response = requests.post(url, json=payload)
print(response.json())
```

`requests` 会自动将数据转换为 JSON 格式，并设置 `Content-Type` 为 `application/json`。

### 2.3 发送表单数据

```python
import requests

url = 'https://api.example.com/submit'
payload = {'key1': 'value1', 'key2': 'value2'}

# 适合 POST、PUT 请求
response = requests.post(url, data=payload)
print(response.text)
```

`requests` 会把 `Content-Type` 设置为 `application/x-www-form-urlencoded` 格式。

### 2.4 发送二进制数据

```python
import requests

url = 'https://api.example.com/upload'
binary_data = b'\x89PNG\r\n\x1a\n\x00\x00\x00...'

# 适合 POST、PUT 请求
response = requests.post(url, data=binary_data, headers={'Content-Type': 'application/octet-stream'})
print(response.text)
```

当发送二进制数据（如视频、音频、图像、protobuf数据等）时，确保 `Content-Type` 设置为 `application/octet-stream` 或其他适当的 MIME 类型。

### 2.5 文件上传

```python
import requests

url = 'https://api.example.com/upload'
files = {'file': open('report.csv', 'rb')}

# 适合 POST、PUT 请求
response = requests.post(url, files=files)
print(response.text)
```

`requests` 会把 `Content-Type` 设置为 `multipart/form-data`，并处理文件边界和编码。