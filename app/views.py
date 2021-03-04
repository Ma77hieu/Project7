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


@app.route('/parser', methods=['POST'])
def parser():
    userInput = request.form.get("question")
    # userInput = request.data
    print("donnée reçue du formulaire: {}".format(userInput))
    # userInput = "Bonsoir Grandpy, j'espère que tu as passé une belle semaine. Est-ce que tu pourrais m'indiquer l'adresse de la tour eiffel? Merci d'avance et salutations à Mamie."
    # print(userInput)
    userQuestion = "<strong>Vous:</strong> " + userInput
    parsed_user_input = parse(userInput)
    print("PARSED:{}".format(parsed_user_input))
    print("TRIMMED: {}".format(trim(parsed_user_input)))
    correct_input = trimSpace(trim(parsed_user_input))
    if correct_input != "no_location":
        summary = getSummary(correct_input)
        parsedTextDisplayed = "<strong>GrandPyBot:</strong> " + summary
        lat = getCoordinates(correct_input)[0]
        lon = getCoordinates(correct_input)[1]
        location_detected = True
    else:
        parsedTextDisplayed = "<strong>GrandPyBot:</strong> Tu es sûr qu'il y a un lieu dans ta question?"
        lat = 0
        lon = 0
        location_detected = False

    return jsonify(userMessage=userQuestion,
                   apiAnswer=parsedTextDisplayed,
                   latitude=lat,
                   longitude=lon,
                   location=location_detected)


if __name__ == "__main__":
    app.run()
