from flask import Flask, redirect, request, jsonify,session

app = Flask(__name__)
app.secret_key = 'sdasfljs3zs6'

# 路由
@app.route('/')
def hello_flask():
    return 'hello flask'


@app.route('/index')
def hello():
    return 'hello world'


# 路由  自定义字符串变量(默认)  后面加斜杠，网址可以不加(系统自动加)
@app.route('/id/<name>/')
def hey(name):
    return 'hey %s' % name


# 路由   定义整形变量  也可以为float,path  后面不加斜杠,网址必须不加(唯一性)
@app.route('/my/<int:number>')
def get_mynumber(number):
    return 'number %s' % (number + number)


# 重定向
@app.route('/baidu')
def baidu():
    return redirect('https:/www.baidu.com')


#POST请求，默认为GET
@app.route('/test/myfirst', methods=['POST'])
def myfirst():
    try:
        my_json = request.get_json()
        print(my_json)
        n = my_json.get('name')
        a = my_json.get('age')
        if not all([n,a]):
            return jsonify(msg='缺少参数')
        a+=10
        return jsonify(name=n, age=a)
    except Exception as e:
        print(e)
        return jsonify(msg='出错了哦')

#登录
@app.route('/try/login',methods=['POST'])
def login():
    '''
    账号：username admin123
    密码：123456
    '''
    get_data = request.get_json()
    username = get_data.get('username')
    password = get_data.get('password')
    if not all([username,password]):
        return jsonify(msg='请输入完整的账号密码！')
    if username =='admin123' and password== '123456':
        #如果验证通过,保存登陆状态在session中
        session['username'] = username
        return jsonify(msg = '登录成功')
    else:
        return jsonify(msg = '账号或密码错误！')


#检查登录状态
@app.route('/session',methods=['GET'])
def check_sess():
    username = session.get('username')
    if username is not None:
        return jsonify(username=username)
    else:
        return jsonify(msg = '没登录,请先登录')

#退出
@app.route('/try/logout',methods=['GET'])
def logout():
    session.clear()
    return jsonify(msg = '退出登录成功！')

if __name__ == '__main__':
    app.run()
