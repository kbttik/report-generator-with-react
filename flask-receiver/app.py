# coding: utf-8
from flask import Flask, render_template, request
import pdb

# Webサーバインスタンスの生成
app = Flask(__name__) 

# http://0.0.0.0:5000/にリクエストが来たときの処理
@app.route("/")
def index():
    return "Hello Flask!"

@app.route('/printer', methods=["POST"])
def print_data():
    pdb.set_trace()
    #print(request.get_data())
    f = open('from.html', "w")
    f.write(request.get_data(as_text=True))
    f.close()
    return "success!"

if __name__ == "__main__":
    # webサーバーの立ち上げ
    app.run(host='0.0.0.0', port=5000, debug=True)

