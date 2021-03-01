from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test32')
def test32():
    return "Test32563"


@app.route('/parser', methods=['POST'])
def parser():
    # userInput = textToParse
    # userInput = request.form["question"]
    # print(request.form["question"])
    userInput = str(request.form.get('question'))
    print(request.form.get('question'))
    print(userInput)
    userQuestion = "Vous: " + userInput
    parsedTextDisplayed = "GrandPyBot: " + userInput
    return (jsonify(userMessage=userQuestion, apiAnswer=parsedTextDisplayed))


if __name__ == "__main__":
    app.run()
