# coding: utf-8
from flask import Flask, render_template, request
# from flask_restful import Api
from src.database import init_db, db
from src.models import Report, Tag
import pdb

# Webサーバインスタンスの生成
app = Flask(__name__) 
app.config.from_object('src.config.Config')
init_db(app)

# http://0.0.0.0:5000/にリクエストが来たときの処理
@app.route("/")
def index():
    return "Please, Post to /printer"

@app.route('/printer', methods=["POST"])
def print_data():
    pdb.set_trace()
    #print(request.get_data())
    #f = open('/mnt/flask-receiver/reports/test_from.html', "w")
    #f.write(request.get_data(as_text=True))
    #f.close()
    return "success!"

if __name__ == "__main__":
    # webサーバーの立ち上げ
    app.run(host='0.0.0.0', port=5000, debug=True)

