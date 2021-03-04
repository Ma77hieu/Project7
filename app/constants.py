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

SUMMARY_API_OK = "La tour Eiffel est une tour de fer puddlé de 324 mètres de hauteur située à Paris, à l’extrémité nord-ouest du parc du Champ-de-Mars en bordure de la Seine dans le 7e arrondissement. Son adresse officielle est 5, avenue Anatole-France."

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
            "revisions": "https://fr.wikipedia.org/wiki/Invalides?action=history",
            "edit": "https://fr.wikipedia.org/wiki/Invalides?action=edit",
            "talk": "https://fr.wikipedia.org/wiki/Discussion:Invalides"
        },
        "mobile": {
            "page": "https://fr.m.wikipedia.org/wiki/Invalides",
            "revisions": "https://fr.m.wikipedia.org/wiki/Special:History/Invalides",
            "edit": "https://fr.m.wikipedia.org/wiki/Invalides?action=edit",
            "talk": "https://fr.m.wikipedia.org/wiki/Discussion:Invalides"
        }
    },
    "extract": "Invalides peut désigner :à Berlin :\nle cimetière des Invalides (Invalidenfriedhof)\nla rue des Invalides (Invalidenstraße)à Bruxelles :\nle boulevard des Invalidesà Paris :\nl'hôtel des Invalides\nle quartier des Invalides\nla gare des Invalides\nla ligne des Invalides\nla station de métro Invalides sur les lignes 8 et 13 du métro de Paris\nle boulevard des Invalides\nle pont des Invalides\nla section des Invalides, pendant la Révolution française\nle colloque des Invalides\nl'esplanade des Invalides",
    "extract_html": "<p><b>Invalides</b> peut désigner :</p><ul><li>à Berlin :\n<ul><li>le cimetière des Invalides <i>(Invalidenfriedhof)</i></li>\n<li>la rue des Invalides <i>(Invalidenstraße)</i></li></ul></li></ul><ul><li>à Bruxelles :\n<ul><li>le boulevard des Invalides</li></ul></li></ul><ul><li>à Paris :\n<ul><li>l'hôtel des Invalides</li>\n<li>le quartier des Invalides</li>\n<li>la gare des Invalides</li>\n<li>la ligne des Invalides</li>\n<li>la station de métro <span><i>Invalides</i></span> sur les lignes 8 et 13 du métro de Paris</li>\n<li>le boulevard des Invalides</li>\n<li>le pont des Invalides</li>\n<li>la section des Invalides, pendant la Révolution française</li>\n<li>le colloque des Invalides</li>\n<li>l'esplanade des Invalides</li></ul></li></ul>"
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
