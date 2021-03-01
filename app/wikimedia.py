import requests
import json

# # Exemple de requete pour avoriu el titre
# https://fr.wikipedia.org/w/api.php?action=query&list=search&srlimit=1&format=json&srsearch=tour%20eiffel

# #exemple pour le summary
# https://fr.wikipedia.org/api/rest_v1/page/summary/Tour%20Eiffel


def get_wikimedia_page_title(location):
    # for letter in location:
    #     if letter == " ":
    #         letter = "%20"
    #     else:
    #         pass
    # print(location)
    # # location_no_space
    title_api_url = (
        """https://fr.wikipedia.org/w/api.php?
        action=query&prop=revisions&rvslots=*&rvprop=content
        &formatversion=2&format=json&titles="""
        + location)

    print(title_api_url)
    exact_page_title = requests.get(title_api_url)
    title_json = json.loads(exact_page_title.content.decode('utf-8'))
    print(title_json)
# self.product_name = p_json["products"][prod]["product_name_fr"]
# if "nutriscore_grade" in p_json["products"][prod]:
#     self.nutriscore = p_json["products"][prod]["nutriscore_grade"]
# self.stores = p_json["products"][prod]["stores"]
# self.url = p_json["products"][prod]["url"]
# self.product.insert_product(self.product_name, self.nutriscore,
#                             self.stores, self.url, cat_name)
# page_title = requests.get()


if (__name__ == "__main__"):
    get_wikimedia_page_title("tour_eiffel")
