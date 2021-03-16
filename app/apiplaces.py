"""
Data extraction from places API
"""
import os
import requests
import json
import app.constants as C
from decouple import config
API_KEY_PLACES = config('PLACES')
# API_KEY_PLACES = os.environ.get("API_KEY_PLACES")


def get_places_info(location):
    """
    Retrieve the adress, name and coordinates of a text query
    """
    title_api_url = (
        "https://maps.googleapis.com/maps/api/"
        "place/findplacefromtext/json"
        "?key=" + API_KEY_PLACES +
        "&inputtype=textquery&fields=formatted_address,geometry,name&input="
        + location)
    # print(title_api_url)
    exact_page_infos = requests.get(title_api_url)
    # print(exact_page_infos.text)
    infos_json = json.loads(exact_page_infos.content.decode('utf-8'))
    print("infos json {}".format(infos_json))
    print("infos json status{}".format(infos_json["status"]))
    # print(infos_json)
    if infos_json["status"] == 'ZERO_RESULTS':
        print("pas de lieu trouvé")
        return C.NO_ADDRESS_FOUND, 0, 0, False
    else:
        exact_address = infos_json["candidates"][0]["formatted_address"]
        print("\nexact address: {}".format(exact_address))
        lat = infos_json["candidates"][0]["geometry"]["location"]["lat"]
        lon = infos_json["candidates"][0]["geometry"]["location"]["lng"]
        print("\nlat: {}".format(lat))
        print("\nlon: {}".format(lon))
        return exact_address, lat, lon, True


if (__name__ == "__main__"):
    get_places_info("open+'%20'+classrooms")
