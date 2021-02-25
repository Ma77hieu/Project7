from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test32')
def test32():
    return "Test32563"


@app.route('/parser', methods=['GET', 'POST'])
def parser():
    userInput = str(request.form.get('question'))
    userMessDisplay = "Vous: " + str(request.form.get('question'))
    apiAnswer = "GrandPyBot: " + userInput
    return render_template('index.html', parsedTextDisplayed=apiAnswer, userQuestion=userMessDisplay)


if __name__ == "__main__":
    app.run()
