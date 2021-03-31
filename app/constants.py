"""Constants used for this application
"""

TITLE_API_NOT_FOUND = {
    "batchcomplete": "",
    "query": {
        "search": []
    }
}

TITLE_API_OK = {
    "batchcomplete": "",
    "query": {
        "search": [
            {
                "ns": 0,
                "title": "Tour Eiffel",
                "pageid": 1359783,
                "size": 132731,
                "wordcount": 19852,
                "snippet": "",
                "timestamp": "2021-02-24T20:30:41Z"
            }
        ]
    }
}

SUMMARY_API_OK_2 = {
    "type": "standard",
    "title": "Tour Eiffel",
    "displaytitle": "Tour Eiffel",
    "namespace": {
        "id": 0,
        "text": ""
    },
    "wikibase_item": "Q243",
    "titles": {
        "canonical": "Tour_Eiffel",
        "normalized": "Tour Eiffel",
        "display": "Tour Eiffel"
    },
    "pageid": 1359783,
    "thumbnail": {
        "source": ("https://upload.wikimedia.org/"
                   "wikipedia/commons/thumb/a/a8/Tour_Eiffel_Wikimedia_Commons"
                   ".jpg/173px-Tour_Eiffel_Wikimedia_Commons.jpg"),
        "width": 173,
        "height": 320
    },
    "originalimage": {
        "source": ("https://upload.wikimedia.org/"
                   "wikipedia/commons/a/a8/Tour_Eiffel_Wikimedia_Commons.jpg"),
        "width": 2900,
        "height": 5367
    },
    "lang": "fr",
    "dir": "ltr",
    "revision": "180764049",
    "tid": "81cd45b0-8a5c-11eb-91c9-ad2ddaff5431",
    "timestamp": "2021-03-11T12:21:37Z",
    "description": "monument de la ville de Paris, France",
    "description_source": "central",
    "coordinates": {
        "lat": 48.858296,
        "lon": 2.294479
    },
    "content_urls": {
        "desktop": {
            "page": "https://fr.wikipedia.org/wiki/Tour_Eiffel",
            "revisions": ("https://fr.wikipedia.org/"
                          "wiki/Tour_Eiffel?action=history"),
            "edit": "https://fr.wikipedia.org/wiki/Tour_Eiffel?action=edit",
            "talk": "https://fr.wikipedia.org/wiki/Discussion:Tour_Eiffel"
        },
        "mobile": {
            "page": "https://fr.m.wikipedia.org/wiki/Tour_Eiffel",
            "revisions": ("https://fr.m.wikipedia.org/"
                          "wiki/Special:History/Tour_Eiffel"),
            "edit": "https://fr.m.wikipedia.org/wiki/Tour_Eiffel?action=edit",
            "talk": "https://fr.m.wikipedia.org/wiki/Discussion:Tour_Eiffel"
        }
    },
    "extract": (
        "La tour Eiffel est une tour de fer "
        "puddlé de 324 mètres de hauteur située à Paris,"
        " à l’extrémité"
        " nord-ouest du parc du Champ-de-Mars "
        "en bordure de la Seine"
        " dans le 7e arrondissement. Son adresse officielle est 5, "
        "avenue Anatole-France."),
    "extract_html": (
        "<p>La <b>tour Eiffel</b> est une tour de fer "
        "puddlé de 324 mètres de hauteur située à Paris,"
        " à l’extrémité nord-ouest du parc du Champ-de-Mars"
        " en bordure de la Seine dans le "
        "<span><abbr class=\"abbr\">7<sup>e</sup></abbr>"
        " arrondissement</span>. Son adresse officielle est 5, "
        "avenue Anatole-France.</p>")
}
SUMMARY_API_OK = (
    "La tour Eiffel est une tour de fer "
    "puddlé de 324 mètres de hauteur située à Paris,"
    " à l’extrémité"
    " nord-ouest du parc du Champ-de-Mars "
    "en bordure de la Seine"
    " dans le 7e arrondissement. Son adresse officielle est 5, "
    "avenue Anatole-France.")

SUMMARY_API_AMBIGUOUS = {
    "type": "disambiguation",
    "title": "Invalides",
    "displaytitle": "Invalides",
    "namespace": {
        "id": 0,
        "text": ""
    },
    "wikibase_item": "Q1175369",
    "titles": {
        "canonical": "Invalides",
        "normalized": "Invalides",
        "display": "Invalides"
    },
    "pageid": 137578,
    "lang": "fr",
    "dir": "ltr",
    "revision": "158081386",
    "tid": "16245530-06b1-11eb-9d3d-353e0fed7097",
    "timestamp": "2019-04-02T13:48:21Z",
    "description": "page d'homonymie de Wikimedia",
    "description_source": "central",
    "content_urls": {
        "desktop": {
            "page": "https://fr.wikipedia.org/wiki/Invalides",
            "revisions": ("https://fr.wikipedia.org/wiki"
                          "/Invalides?action=history"),
            "edit": "https://fr.wikipedia.org/wiki/Invalides?action=edit",
            "talk": "https://fr.wikipedia.org/wiki/Discussion:Invalides"
        },
        "mobile": {
            "page": "https://fr.m.wikipedia.org/wiki/Invalides",
            "revisions": ("https://fr.m.wikipedia.org/"
                          "wiki/Special:History/Invalides"),
            "edit": "https://fr.m.wikipedia.org/wiki/Invalides?action=edit",
            "talk": "https://fr.m.wikipedia.org/wiki/Discussion:Invalides"
        }
    },
    "extract": ("Invalides peut désigner :"
                "à Berlin :\nle cimetière des Invalides (Invalidenfriedhof)"
                "\nla rue des Invalides (Invalidenstraße)"
                "à Bruxelles :\nle boulevard des Invalides"
                "à Paris :\nl'hôtel des Invalides\nle quartier des Invalides"
                "\nla gare des Invalides\nla ligne des Invalides"
                "\nla station de métro Invalides sur les lignes 8 et 13 "
                "du métro de Paris\nle boulevard des Invalides"
                "\nle pont des Invalides\nla section des Invalides, "
                "pendant la Révolution française\nle colloque des Invalides"
                "\nl'esplanade des Invalides"),
    "extract_html": ("<p><b>Invalides</b> peut désigner :"
                     "</p><ul><li>à Berlin :\n<ul><li>"
                     "le cimetière des Invalides"
                     " <i>(Invalidenfriedhof)</i></li>"
                     "\n<li>la rue des Invalides"
                     " <i>(Invalidenstraße)</i></li></ul></li></ul><ul><li>"
                     "à Bruxelles :\n<ul>"
                     "<li>le boulevard des Invalides</li></ul></li></ul>"
                     "<ul><li>à Paris :\n<ul><li>l'hôtel des Invalides</li>"
                     "\n<li>le quartier des Invalides</li>\n"
                     "<li>la gare des Invalides</li>\n<li>"
                     "la ligne des Invalides</li>\n<li>"
                     "la station de métro <span><i>Invalides</i></span>"
                     " sur les lignes 8 et 13 du métro de Paris</li>\n"
                     "<li>le boulevard des Invalides</li>\n<li>"
                     "le pont des Invalides</li>\n"
                     "<li>la section des Invalides, "
                     "pendant la Révolution française</li>\n<li>"
                     "le colloque des Invalides</li>\n<li>"
                     "l'esplanade des Invalides</li></ul></li></ul>")
}

COORDINATES_API_OK = {
    "batchcomplete": "",
    "query": {
        "normalized": [
            {
                "from": "tour Eiffel",
                "to": "Tour Eiffel"
            }
        ],
        "pages": {
            "1359783": {
                "pageid": 1359783,
                "ns": 0,
                "title": "Tour Eiffel",
                "coordinates": [
                    {
                        "lat": 48.858296,
                        "lon": 2.294479,
                        "primary": "",
                        "globe": "earth"
                    }
                ]
            }
        }
    }
}

COORDINATES_API_NO_DATA = {
    "batchcomplete": "",
    "query": {
        "normalized": [
            {
                "from": "Napoléon_Ier",
                "to": "Napoléon Ier"
            }
        ],
        "pages": {
            "676806": {
                "pageid": 676806,
                "ns": 0,
                "title": "Napoléon Ier"
            }
        }
    }
}


test_se_trouve = ("Salut grandpy! Comment s'est passé"
                  " ta soirée avec Grandma hier soir? Au fait,"
                  " pendant que j'y pense, pourrais-tu m'indiquer "
                  "où se trouve le musée d'art et d'histoire de Fribourg,"
                  " s'il te plaît?")

test_adresse_de = (
    "Bonsoir Grandpy, j'espère que tu as passé"
    " une belle semaine. Est-ce que tu pourrais m'indiquer "
    "l'adresse de la tour eiffel? Merci d'avance et salutations à Mamie.")

test_se_situent = (
    "Dis moi Grandpy, tu pourrais me dire ou se situent les Invalides?")

test_situées = (
    "Salut Grandpy, j'espère que tu vas bien."
    " Dis moi, il me semble que tu y es déjà allé, "
    "pourrais tu m'indiquer où sont situées les chutes du Niagara?")

ANSWER_NO_LOCATION_FOUND = (
    "Je n'ai pas d'informations plus détaillées sur ce lieu. "
    "Ne l'as tu pas mal orthographié ou oublié des majuscules? "
    "N'hésite pas à regarder le titre de la page wikipedia correspondante"
    " en respectant bien les majuscules ;-)")

ANSWER_AMBIGUITY = (
    "Ce nom de lieu correspond"
    " à plusieurs choses, essaye d'être plus précis(e)")

ANSWER_NO_LOCATION_INPUT = (
    "Tu es sûr de bien me demander une localisation?"
    " Voici un exemple: où se trouve la tour Eiffel?")

NO_ADDRESS_FOUND = "Je n'ai pas trouvé d'adresse"
