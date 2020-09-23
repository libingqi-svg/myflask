# -*- coding: utf-8 -*-
"""
@Time    : 2020/7/27 17:17
@Author  : Jaxson
@FileName: test_restful1.py
@Software: PyCharm
"""

"""
flask restful 开发API接口
"""
from flask import Flask, request
from flask_restful import Api, Resource, reqparse

# Flask相关变量声明
app = Flask(__name__)

# flask_restful API对象
api = Api(app)

# 创建请求参数解析对象
parser_put = reqparse.RequestParser()
# 添加验证字段，以及验证信息
parser_put.add_argument('user', type=str, required=True, help='need user')  # required 限制为非空
parser_put.add_argument('pwd', type=str, required=True, help='need pwd')


# 实现逻辑代码
def to_add(arg1, arg2):
    return str(arg1) + str(arg2)


# 继承自flask_restful.Resource类
class Todo(Resource):
    def post(self):  # 定义来自请求的方法, 例如get,post
        args = parser_put.parse_args()
        user = args.get('user')
        pwd = args['pwd']
        info = {'info': to_add(user, pwd)}
        return info


# 设置路由(每个继承Resource的类只能设置一个对应的路由)
api.add_resource(Todo, '/users')
# api.add_resource(Todo, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
