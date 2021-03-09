"""
Application routes definitions
"""
from flask import Flask, request, render_template, jsonify
import json
from .inputParser import parse as parse
# from .inputParser import trim_article_location as trim
# from .wikimedia import eliminate_space_char as trimSpace
# from .wikimedia import get_wikimedia_page_title as getSummary
from .wikimedia import get_wikimedia_page_summary as getSummary
# from .wikimedia import get_wikimedia_coordinates as getCoordinates
from .apiplaces import get_places_info as getInfos
import app.constants as C


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
    # print("donnée reçue du formulaire: {}".format(userInput))
    userQuestion = "<strong>Vous:</strong> " + userInput
    location = parse(userInput)
    if location != "no_location_in_input":
        summary = getSummary(location)
        all_coordinates_data = getInfos(location)
        adress = all_coordinates_data[0]
        lat = all_coordinates_data[1]
        lon = all_coordinates_data[2]
        displayLocation = all_coordinates_data[3]
        print("SUMMARY RETURNED : {}".format(summary))
        parsedTextDisplayed2 = "<strong>GrandPyBot:</strong> " + summary
        if adress == C.NO_ADDRESS_FOUND:
            parsedTextDisplayed1 = "<strong>GrandPyBot:</strong> "+C.NO_ADDRESS_FOUND
        else:
            parsedTextDisplayed1 = "<strong>GrandPyBot:</strong> L'adresse que tu cherches est:"+adress

    else:
        parsedTextDisplayed1 = "<strong>GrandPyBot:</strong>"+C.ANSWER_NO_LOCATION_INPUT
        parsedTextDisplayed2 = ""
        lat = 0
        lon = 0
        displayLocation = False

        # userQuestion=

    return jsonify(userMessage=userQuestion,
                   apiAnswer1=parsedTextDisplayed1,
                   apiAnswer2=parsedTextDisplayed2,
                   latitude=lat,
                   longitude=lon,
                   location=displayLocation)


if __name__ == "__main__":
    app.run()
