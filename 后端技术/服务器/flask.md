# Flask

文档：https://flask.palletsprojects.com/en/2.0.x/

依赖
- Werkzeug，德语，工具的意思。werkzeug 是一个实现了 WSGI 的 python库，或者说工具包；
- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)，模板引擎，可以结合代码和HTML语言，返回灵活的页面。
- MarkupSafe，和 Jinja 一起引用，用于网页文本中特殊字符的转义。
- ItsDangerous，用于数据签名和校验，主要用来保护 flask session cookie；
- Click，用来生成命令行工具；

### Debug mode
```bash
$ export FLASK_APP=hello
$ export FLASK_ENV=development
$ flask run
```

### HTML Escaping（转义）
```python
from markupsafe import escape

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"
```

### Variable Rules
针对 URL 做一些简单的解析工作，支持 `string/int/float/path/uuid` 类型。
```python
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'
```

### URL Binding

```python
from flask import url_for
```

### HTTP Methods
```python
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
```

### Static Files

```
url_for('static', filename='style.css')
```

### Rendering Templates 渲染模板
```python
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
```
需要把模板文件 `hello.html` 放在 `./templates/` 目录下。

### Request Data

```python
from flask import request

request.method                  # GET/POST 方法
request.form["username"]        # POST 表格参数
request.args.get('key', '')     # GET 参数
request.files['filename']       # 上传文件
```

### Cookie
读取 cookie
```python
from flask import request

@app.route('/')
def index():
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.
```

存储 Cookie
```python
from flask import make_response

@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp
```

### Redirects and Errors
重定向
```python
from flask import abort, redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()
```

定制化错误页面
```python
from flask import render_template

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
```

### About Response
Flask 最终会返回一个 reponse 对象，但是 route 函数不一定，有下面几个转换规则
1. 如果是一个 Reponse 对象，直接返回
2. 如果是一个字符串，会创建 Response 对象；
3. 如果是一个字典，会调用 jsonify 函数
4. 如果是一个元组，比如 (response, status), (response, headers), (response, status, headers) 这几种返回类型。
5. 否则创建一个默认的 Response 对象。

### Session
下面的代码展示了登录、登出的一个示例，在此过程中，flask 把用户名存储在 Session 字典中。
```
from flask import Flask
from flask import redirect, request, session, url_for


app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

```

### Blueprinta
可以看做是 application 的子模块，可以用来构建大型的项目。

参考 flask 的相关文档：https://flask.palletsprojects.com/en/1.1.x/blueprints/
