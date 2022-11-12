import json
from flask import Flask, request
from service import wordCloud
from flask_cors import CORS
import top100

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/wordCloud', methods=["GET", "POST"])
def hello_world():
    json_data = request.get_json()
    cid = json_data['cid']
    data = wordCloud.spider_page(cid)
    return '{"code": 200, "message": "查询成功", "data":' + json.dumps(data) + '}'


@app.route('/top100', methods=["GET", "POST"])
def get_top100():
    return top100.top100()


if __name__ == '__main__':
    app.run()
