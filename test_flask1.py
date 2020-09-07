from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/test_1.0', methods=['GET'])
# @app.route('/test_1.0', methods=['POST'])
def check():
    return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': False}
    # GET
    # 判断入参是否为空
    if request.args is None:   #解析url参数(get请求方式获取数据)
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    # 获取传入的params参数
    get_data = request.args.to_dict()
    name = get_data.get('name')
    age = get_data.get('age')

    # POST
    # 判断传入的json数据是否为空
    # if not request.get_data():   #获取传入的数据(保留原格式)
    #     return_dict['return_code'] = '5004'
    #     return_dict['return_info'] = '请求参数为空'
    #     return json.dumps(return_dict, ensure_ascii=False)
    # # 获取传入的参数
    # get_data = request.get_data()
    # # 传入的参数为bytes，需要转化成json
    # get_data = json.loads(get_data)
    # name = get_data.get('name')
    # age = get_data['age']

    # 对参数进行操作
    return_dict['result'] = tt(name, age)
    return json.dumps(return_dict, ensure_ascii=False)


# 功能函数
def tt(name, age):
    result_str = "%s今年%s岁" % (name, age)
    return result_str


if __name__ == "__main__":
    app.run(debug=True)
