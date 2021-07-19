from flask import Flask

app = Flask(__name__)

#定义接口地址
@app.route('/hello')
def hello_world():
    return '你好，欢迎来到Flask!'


if __name__ == '__main__':
    app.run()
