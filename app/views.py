"""
Application routes definitions
"""
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
    """
    Extract location from userInput.
    Returns formatted userInput, api response, coordinates for the map
    """
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
    print("TRIMMED SPACE: {}".format(correct_input))
    if correct_input != "no_location":
        summary = getSummary(correct_input)
        print("SUMMARY RETURNED : {}".format(summary))
        if summary not in ["ambiguity", "no title found"]:
            parsedTextDisplayed = "<strong>GrandPyBot:</strong> " + summary
            lat = getCoordinates(correct_input)[0]
            lon = getCoordinates(correct_input)[1]
            displayLocation = True
        else:
            lat = 0
            lon = 0
            displayLocation = False
            if summary == "no title found":
                parsedTextDisplayed = "<strong>GrandPyBot:</strong> Je n'ai pas compris le nom du lieu dont tu me parles"
            if summary == "ambiguity":
                parsedTextDisplayed = "<strong>GrandPyBot:</strong> Ce nom de lieu correspond à plusieurs choses, essaye d'être plus précis(e)"

    else:
        parsedTextDisplayed = "<strong>GrandPyBot:</strong> Tu es sûr qu'il y a un lieu dans ta question?"
        lat = 0
        lon = 0
        displayLocation = False

    return jsonify(userMessage=userQuestion,
                   apiAnswer=parsedTextDisplayed,
                   latitude=lat,
                   longitude=lon,
                   location=displayLocation)


if __name__ == "__main__":
    app.run()
