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
    char_pos = 0

    for letter in location:
        if letter == " ":
            location = location[:char_pos] + "%20" + location[char_pos+1:]
            char_pos += 1
            print("The location has changed to {}".format(
                location))
        else:
            char_pos += 1
    return location


def get_wikimedia_page_title(location):
    """
    Retrieve the exact name of the page to access its content
    """
    title_api_url = (
        "https://fr.wikipedia.org/w/api.php?action=query&list=search&srlimit=1&format=json&srwhat=nearmatch&srsearch="
        + location)
    # print(title_api_url)
    exact_page_infos = requests.get(title_api_url)
    # print(exact_page_infos.text)
    infos_json = json.loads(exact_page_infos.content.decode('utf-8'))
    # print(infos_json)
    exact_page_title = infos_json["query"]["search"][0]["title"]
    print("\none matching page found: {}".format(exact_page_title))
    return exact_page_title


def get_wikimedia_page_summary(page_title):
    """
    Retrieve the summary of a page thanks to its title
    """
    summary_api_url = (
        "https://fr.wikipedia.org/api/rest_v1/page/summary/"
        + page_title)
    # print(title_api_url)
    whole_page_infos = requests.get(summary_api_url)
    # print(exact_page_infos.text)
    whole_page_json = json.loads(whole_page_infos.content.decode('utf-8'))
    # print(infos_json)
    page_extract = whole_page_json["extract"]
    print("\n#######\nInfos\n#######\n{}".format(page_extract))


if (__name__ == "__main__"):
    correct_input = eliminate_space_char(
        "Tour Eiffel")
    correct_title = get_wikimedia_page_title(
        correct_input)
    get_wikimedia_page_summary(correct_title)
# le%20musée%20d'art%20et%20d'histoire%20de%20Fribourg
