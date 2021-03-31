from flask import jsonify
from app.inputParser import parse as parse
from app.wikimedia import WikiAnswer
from app.apiplaces import Places
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
            summary = WikiAnswer(location).summary
            all_coordinates_data = Places(location)
            adress = all_coordinates_data.exact_address
            lat = all_coordinates_data.lat
            lon = all_coordinates_data.lon
            displayLocation = all_coordinates_data.location_found
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


# if __name__ == "__main__":
#     test = Answer("situe Bordeaux")
