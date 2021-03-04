import requests
import json

# # Exemple de requete pour avoriu el titre
# https://fr.wikipedia.org/w/api.php?action=query&list=search&srlimit=1&format=json&srsearch=tour%20eiffel

# #exemple pour le summary
# https://fr.wikipedia.org/api/rest_v1/page/summary/Tour%20Eiffel


def eliminate_space_char(location):
    """
    Replace the space character with %20
    Mandatory to insert location in the api request
    """
    if location != "no_location":
        print("lieu en entrée {}".format(location))
        location = location.replace(' ', '%20')
        print("lieu avec les %20: {}".format(location))
    else:
        pass
    return location


def get_wikimedia_page_title(location):
    """
    Retrieve the exact name of the page to access its content
    """
    title_api_url = (
        "https://fr.wikipedia.org/w/api.php?action=query&list=search&srlimit=1&format=json&srwhat=nearmatch&srsearch="
        + eliminate_space_char(location))
    # print(title_api_url)
    exact_page_infos = requests.get(title_api_url)
    # print(exact_page_infos.text)
    infos_json = json.loads(exact_page_infos.content.decode('utf-8'))
    # print(infos_json)
    exact_page_title = infos_json["query"]["search"][0]["title"]
    print("\none matching page found: {}".format(exact_page_title))
    return exact_page_title


def get_wikimedia_page_summary(userInput):
    """
    Retrieve the summary of a page thanks to its title
    """
    summary_api_url = (
        "https://fr.wikipedia.org/api/rest_v1/page/summary/"
        + get_wikimedia_page_title(userInput))
    # print(title_api_url)
    whole_page_infos = requests.get(summary_api_url)
    # print(exact_page_infos.text)
    whole_page_json = json.loads(whole_page_infos.content.decode('utf-8'))
    # print(infos_json)
    page_extract = whole_page_json["extract"]
    print("\n#######\nInfos\n#######\n{}".format(page_extract))
    return page_extract


def get_wikimedia_coordinates(userInput):
    """
    Retrieve the coordinates of a wikir essource thanks to its title
    """
    coordinates_api_url = (
        "https://fr.wikipedia.org/w/api.php?action=query&prop=coordinates&format=json&titles="
        + get_wikimedia_page_title(userInput))
    # print(title_api_url)
    whole_page_infos = requests.get(coordinates_api_url)
    # print(exact_page_infos.text)
    whole_page_json = json.loads(whole_page_infos.content.decode('utf-8'))
    # print(infos_json)
    partial_JSON = whole_page_json["query"]["pages"]
    page_id = str(list(partial_JSON.keys())[0])
    # page_id = page_id.replace("'", '"')
    lat = whole_page_json["query"]["pages"][page_id]["coordinates"][0]["lat"]
    lon = whole_page_json["query"]["pages"][page_id]["coordinates"][0]["lon"]
    print("\n#######\nInfos\n#######\nlatitude:{}\nlongitude: {}".format(lat, lon))
    return lat, lon


if (__name__ == "__main__"):
    # correct_input=eliminate_space_char(
    #     "Tour Eiffel")
    # correct_title=get_wikimedia_page_title(
    #     correct_input)
    # get_wikimedia_page_summary(correct_title)
    # le%20musée%20d'art%20et%20d'histoire%20de%20Fribourg
    get_wikimedia_page_summary(
        "chutes du Niagara")
    get_wikimedia_coordinates("tour Eiffel")
