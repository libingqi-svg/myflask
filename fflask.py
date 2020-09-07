# -*- coding: utf-8 -*-
'''
@Time    : 2020/9/7 11:49
@Author  : Jaxson
@FileName: fflask.py
@Software: PyCharm
'''

from flask import Flask, request
import json

app = Flask(__name__)


# @app.route('/match', methods=['GET'])
@app.route('/match', methods=['POST'])
def user_input():
    return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': False}
    if not request.get_data():
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    get_data = request.get_data()
    get_data = json.loads(get_data)
    # 获取到用户输入的问题
    sentence = get_data.get('sentence')
    result = model(sentence)
    return_dict['result'] = result
    return json.dumps(return_dict, ensure_ascii=False)


# 具体模型处理函数
def model(sentence):
    pass


if __name__ == '__main__':
    app.run(debug=True)
