"""
Data extraction from wikimedia API
"""
import requests
import json
from app.constants import (ANSWER_AMBIGUITY, ANSWER_NO_LOCATION_FOUND)
from app.apiplaces import Places


class WikiAnswer:

    def __init__(self, location):
        self.location = location
        self.title = self.get_wikimedia_page_title(location)
        self.summary = self.get_wikimedia_page_summary(self.title)

    def get_wikimedia_page_title(self, location):
        """
        Retrieve the exact name of the page to access its content
        """
        title_api_url = (
            "https://fr.wikipedia.org/w/api.php?"
            "action=query&list=search&srlimit=1&format=json"
            "&srwhat=nearmatch&srsearch="
            + location)
        infos_json = self.get_json_title(title_api_url)
        # print(infos_json)
        if not infos_json["query"]["search"]:
            print("pas de lieu trouvé")
            return "no title found"
        else:
            exact_page_title = infos_json["query"]["search"][0]["title"]
            print("\none matching page found: {}".format(exact_page_title))
            return exact_page_title

    def get_json_title(self, api_url):
        """
        Send the request to the API and converts the result into JSON    
        """
        exact_page_infos = requests.get(api_url)
        extracted_json = json.loads(exact_page_infos.content.decode('utf-8'))
        return extracted_json

    def get_json_summary(self, api_url):
        """
        Send the request to the API and converts the result into JSON    
        """
        exact_page_infos = requests.get(api_url)
        extracted_json = json.loads(exact_page_infos.content.decode('utf-8'))
        return extracted_json

    def get_wikimedia_page_summary(self, title):
        """
        Retrieve the summary of a page thanks to its title
        """
        if self.get_wikimedia_page_title(title) != "no title found":
            summary_api_url = (
                "https://fr.wikipedia.org/api/rest_v1/page/summary/"
                + self.get_wikimedia_page_title(title))
            whole_page_json = self.get_json_summary(summary_api_url)
            if whole_page_json["type"] == "standard":
                page_extract = whole_page_json["extract"]
                return page_extract
            else:
                return ANSWER_AMBIGUITY
        else:
            return ANSWER_NO_LOCATION_FOUND

    # def get_json_coordinates(api_url):
    #     """
    #     Send the request to the API and converts the result into JSON
    #     """
    #     exact_page_infos = requests.get(api_url)
    #     extracted_json = json.loads(exact_page_infos.content.decode('utf-8'))
    #     return extracted_json

    # def get_wikimedia_coordinates(userInput):
    #     """
    #     Retrieve the coordinates of a wikir essource thanks to its title
    #     """
    #     coordinates_api_url = (
    #         "https://fr.wikipedia.org/w/api.php?"
    #         "action=query&prop=coordinates&format=json&titles="
    #         + get_wikimedia_page_title(userInput))

    #     whole_json = get_json_coordinates(coordinates_api_url)
    #     partial_JSON = whole_json["query"]["pages"]
    #     page_id = str(list(partial_JSON.keys())[0])
    #     if "coordinates" in whole_json["query"]["pages"][page_id]:
    #         lat = whole_json["query"]["pages"][page_id]["coordinates"][0]["lat"]
    #         lon = whole_json["query"]["pages"][page_id]["coordinates"][0]["lon"]
    #     else:
    #         lat = 0
    #         lon = 0
    #     return lat, lon


# if (__name__ == "__main__"):
#     # correct_input=eliminate_space_char(
#     #     "Tour Eiffel")
#     # correct_title=get_wikimedia_page_title(
#     #     correct_input)
#     # get_wikimedia_page_summary(correct_title)
#     # le%20musée%20d'art%20et%20d'histoire%20de%20Fribourg
#     get_wikimedia_page_summary(
#         "tour"+"%20"+"Eiffel")
#     get_wikimedia_coordinates("tour Eiffel")
