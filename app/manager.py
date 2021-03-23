from flask import Flask, request, render_template, jsonify
from app.inputParser import parse as parse
from app.wikimedia import get_wikimedia_page_summary as getSummary
from app.apiplaces import get_places_info as getInfos
from app.constants import (NO_ADDRESS_FOUND, ANSWER_NO_LOCATION_INPUT)


class BotAnswer:
    """
    Extract location from userInput.
    Returns formatted userInput, api response, coordinates for the map
    """

    def __init__(self, userRequest):

        userQuestion = "<strong>Vous:</strong> " + userRequest
        location = parse(userRequest)
        if location != "no_location_in_input":
            summary = getSummary(location)
            all_coordinates_data = getInfos(location)
            adress = all_coordinates_data[0]
            lat = all_coordinates_data[1]
            lon = all_coordinates_data[2]
            displayLocation = all_coordinates_data[3]
            parsedTextDisplayed2 = "<strong>GrandPyBot:</strong> " + summary
            if adress == NO_ADDRESS_FOUND:
                parsedTextDisplayed1 = ("<strong>GrandPyBot:</strong> "
                                        + NO_ADDRESS_FOUND)
            else:
                parsedTextDisplayed1 = ("<strong>GrandPyBot:</strong>"
                                        " L'adresse que tu cherches est: "
                                        + adress)

        else:
            parsedTextDisplayed1 = ("<strong>GrandPyBot:</strong>"
                                    + ANSWER_NO_LOCATION_INPUT)
            parsedTextDisplayed2 = ""
            lat = 0
            lon = 0
            displayLocation = False

        self.response = jsonify(userMessage=userQuestion,
                                apiAnswer1=parsedTextDisplayed1,
                                apiAnswer2=parsedTextDisplayed2,
                                latitude=lat,
                                longitude=lon,
                                location=displayLocation)


if __name__ == "__main__":
    test = Answer("situe Bordeaux")
