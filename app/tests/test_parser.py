from app.inputParser import parse_exple
from app.inputParser import parse


def test_f_parse_return_OK():
    result = parse_exple()
    assert result == "OK"


test_se_trouve = """Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?"""

test_adresse_de = """Bonsoir Grandpy, j'espère que tu as passé une belle semaine. Est-ce que tu pourrais m'indiquer l'adresse de la tour eiffel? Merci d'avance et salutations à Mamie."""

test_se_situent = "Dis moi Grandpy, tu pourrais me dire ou se situent les Invalides?"

test_situées = "Grandpy, au fait, tu sais où sont situées les chutes du Niagara?"


def test_parse_se_trouve():
    result = parse(test_se_trouve)
    assert result == " le musée d'art et d'histoire de Fribourg"


def test_parse_adresse_de():
    result = parse(test_adresse_de)
    assert result == " la tour eiffel"


def test_parse_se_situent():
    result = parse(test_se_situent)
    assert result == " les Invalides"


def test_parse_situées():
    result = parse(test_situées)
    assert result == " les chutes du Niagara"

# EXEMPLES DE TEST
# "Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?"
#  "Bonsoir Grandpy, j'espère que tu as passé une belle semaine. Est-ce que tu pourrais m'indiquer l'adresse de la tour eiffel? Merci d'avance et salutations à Mamie."
