import requests
import json

# # Exemple de requete pour avoriu el titre
# https://fr.wikipedia.org/w/api.php?action=query&list=search&srlimit=1&format=json&srsearch=tour%20eiffel

# #exemple pour le summary
# https://fr.wikipedia.org/api/rest_v1/page/summary/Tour%20Eiffel


def eliminate_space_char(location):
    """
    Replace the space character with %20
    Mandatory to insert location in   the api request
    """
    char_pos = 0

    for letter in location:
        if letter == " ":
            newLocation = location[:char_pos] + "%20"+location[char_pos+1:]
            char_pos += 1
            print("The location has changed from {} to {}".format(
                location, newLocation))
        else:
            char_pos += 1
    return newLocation


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


# self.product_name = p_json["products"][prod]["product_name_fr"]
# if "nutriscore_grade" in p_json["products"][prod]:
#     self.nutriscore = p_json["products"][prod]["nutriscore_grade"]
# self.stores = p_json["products"][prod]["stores"]
# self.url = p_json["products"][prod]["url"]
# self.product.insert_product(self.product_name, self.nutriscore,
#                             self.stores, self.url, cat_name)
# page_title = requests.get()


if (__name__ == "__main__"):
    correct_input = eliminate_space_char("tour eiffel")
    get_wikimedia_page_title(correct_input)
