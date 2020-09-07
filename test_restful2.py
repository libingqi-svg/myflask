# -*- coding: utf-8 -*-
'''
@Time    : 2020/7/27 17:21
@Author  : Jaxson
@FileName: test_restful2.py
@Software: PyCharm
'''

from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort

Tasks = {
    't1': {'task': 'eat an app'},
    't2': {'task': 'play football'},
    't3': {'task': 'watching TV'},
}

app = Flask(__name__)
api = Api(app)


def abort_if_todo_doesnt_exist(t_id):
    if t_id not in Tasks:
        abort(404, message='Todo {} doesnt exist'.format(t_id))


parser = reqparse.RequestParser()
parser.add_argument('task', type=str)


# 更新 删除

class Updata_Delete(Resource):
    def get(self, t_id):  # 根据t_id获取对应的value
        abort_if_todo_doesnt_exist(t_id)
        return Tasks[t_id]

    def delete(self, t_id):  # 根据t_id删除对应的value
        abort_if_todo_doesnt_exist(t_id)
        del Tasks[t_id]
        return 'delete success:{}'.format(t_id)

    def post(self, t_id):  # 判断t_id是否存在，并返回Tasks整个列表
        abort_if_todo_doesnt_exist(t_id)
        return Tasks

    def put(self, t_id):  # 根据t_id添加对应的value，并返回所有值
        args = parser.parse_args()
        value = args['task']
        Tasks[t_id] = {'task': value}
        return Tasks


api.add_resource(Updata_Delete, '/updata_delete/<t_id>')

if __name__ == '__main__':
    app.run(debug=True)
