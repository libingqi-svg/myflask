import random
import requests
import flask, json
from flask import request

app = flask.Flask(__name__)


# 设置路由
@app.route('/accessoriesName', methods=['get', 'post'])
def reg():
    data = json.loads(request.get_data())
    print(data)
    vehicle_model = data.get('vehicle_model')
    vehicle_parts = data.get('vehicle_parts')
    parts = vehicle_parts.split(',')
    dic = {}
    for part in parts:
        price1 = random.randint(31, 300)
        price2 = random.randint(31, 300)  # time.sleep(25)
        dic[part] = {"taobao": price1, "jingd": price2}
    return json.dumps(dic, ensure_ascii=False)


if __name__ == '__main__':
    # 端口号用0.0.0.0，表示局域网和外网都可以访问。
    app.run(debug=True)

    # 测试数据
    CONFIG = {'url': 'http://111.230.203.153:6100/accessoriesName'}
    url = CONFIG['url']
    data = json.dumps(
        {"vehicle_model": "北京现代", "vehicle_code": "Cx4", 'vehicle_parts': "前叶子板,后叶子板", 'vehicle_price': '266'})
    print(data)
    response = requests.post(url=url, data=data, timeout=40)
    print(response.status_code, response.text)
