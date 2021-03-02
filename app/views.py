from flask import Flask, request, render_template, jsonify
import json
from .inputParser import parse as parse
from .inputParser import trim_article_location as trim
from .wikimedia import eliminate_space_char as trimSpace
# from .wikimedia import get_wikimedia_page_title as getSummary
from .wikimedia import get_wikimedia_page_summary as getSummary
from .wikimedia import get_wikimedia_coordinates as getCoordinates


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
    userInput = "Bonsoir Grandpy, j'espère que tu as passé une belle semaine. Est-ce que tu pourrais m'indiquer l'adresse de la tour eiffel? Merci d'avance et salutations à Mamie."
    # print(request.form['question'])
    print(userInput)
    userQuestion = "<strong>Vous:</strong> " + userInput
    parsed_user_input = parse(userInput)
    print("PARSED:{}".format(parsed_user_input))
    print("TRIMMED: {}".format(trim(parsed_user_input)))

    correct_input = trimSpace(trim(parsed_user_input))
    summary = getSummary(correct_input)
    lat = getCoordinates(correct_input)[0]
    lon = getCoordinates(correct_input)[1]
    parsedTextDisplayed = "<strong>GrandPyBot:</strong> " + summary
    return jsonify(userMessage=userQuestion,
                   apiAnswer=parsedTextDisplayed,
                   latitude=lat,
                   longitude=lon)


if __name__ == "__main__":
    app.run()
