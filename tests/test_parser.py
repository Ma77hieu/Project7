from app.parser import parse_exple
from app.parser import parse


def f_parse_return_OK():
    result = parse_exple()
    assert result == "OK"


test_se_trouve = """Salut grandpy! 
Comment s'est passé ta soirée avec Grandma hier soir?
Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve
le musée d'art et d'histoire de Fribourg, s'il te plaît?"""

test_adresse_de = """Bonsoir Grandpy, j'espère que tu as passé une belle semaine. 
Est-ce que tu pourrais m'indiquer l'adresse de la tour eiffel? 
Merci d'avance et salutations à Mamie."""


def parse_se_trouve(test_se_trouve):
    result = parse(test_se_trouve)
    assert result == "le musée d'art et d'histoire de Fribourg"


def parse_adresse_de(test_adresse_de):
    result = parse(test_adresse_de)
    assert result == "la tour eiffel"

# EXEMPLES DE TEST
# "Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?"
#  "Bonsoir Grandpy, j'espère que tu as passé une belle semaine. Est-ce que tu pourrais m'indiquer l'adresse de la tour eiffel? Merci d'avance et salutations à Mamie."
