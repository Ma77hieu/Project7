from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world 235!"


@app.route('/test32')
def test32():
    return "Test32563"


if __name__ == "__main__":
    app.run()
