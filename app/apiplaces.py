"""
Data extraction from places API
"""
import requests
import json
import app.constants as C
from config import API_KEY_PLACES


class Places:

    def __init__(self, location):
        self.location = location
        self.get_places_info(location)

    def get_json(self, api_url):
        """
        Send the request to the API and converts the result into JSON
        """
        exact_page_infos = requests.get(api_url)
        extracted_json = json.loads(exact_page_infos.content.decode('utf-8'))
        return extracted_json

    def get_places_info(self, location):
        """
        Retrieve the adress, name and coordinates of a text query
        """
        title_api_url = (
            "https://maps.googleapis.com/maps/api/"
            "place/findplacefromtext/json"
            "?key=" + API_KEY_PLACES + "&inputtype=textquery"
            "&fields=formatted_address,geometry,name&input="
            + location)
        dataJson = self.get_json(title_api_url)
        if dataJson["status"] == 'ZERO_RESULTS':
            print("pas de lieu trouvé")
            self.location_found = False
            self.lat = 0
            self.lon = 0
            self.exact_address = C.NO_ADDRESS_FOUND

        else:
            self.exact_address = dataJson["candidates"][0]["formatted_address"]
            print("\nexact address: {}".format(self.exact_address))
            self.lat = dataJson["candidates"][0]["geometry"]["location"]["lat"]
            self.lon = dataJson["candidates"][0]["geometry"]["location"]["lng"]
            print("\nlat: {}".format(self.lat))
            print("\nlon: {}".format(self.lon))
            self.location_found = True

# if (__name__ == "__main__"):
#     self.get_places_info("open+'%20'+classrooms")
