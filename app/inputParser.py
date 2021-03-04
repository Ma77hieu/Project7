
def parse_exple():
    # for test purpose
    return "OK"


def parse(stringToParse):
    """
    Locate and extract a location from a text
    """
    parsedString = str
    parsing_done = False
    length = len(stringToParse)
    importantWordBefore = ["adresse de", "adresse des", "se trouve", "se trouvent",
                           "situe ", "situent", "situé ", "situés", "situées", "située"]
    importantWordAfter = [",", "?", "."]
    if stringToParse[-1] not in importantWordAfter:
        stringToParse = stringToParse+","
    for beforeWord in importantWordBefore:
        if beforeWord in stringToParse:
            breakWordLength = len(beforeWord)
            startIndex = stringToParse.find(beforeWord)+breakWordLength
            parsedString = stringToParse[startIndex:length+1]
            while parsing_done == False:
                for afterWord in importantWordAfter:
                    if afterWord in parsedString:
                        endIndex = parsedString.find(afterWord)
                        parsedString = parsedString[0:endIndex]
                        parsing_done = True
                    else:
                        pass
            print(parsedString)
            return parsedString

    if parsing_done == False:
        print("Pas de lieu identifié par le parser")
        return "no_location"


def trim_article_location(location):
    """
    Remove article in the location like "la" in "la tour eiffel"
    """
    articles = ["la ", "le ", "les ", "l'"]
    trim_done = False
    while trim_done != True:
        for article in articles:
            if article in location[:5]:
                trimmedLocation = location.replace(article, '')
                trim_done = True
                print(trimmedLocation)
                return trimmedLocation
        if trim_done == False:
            print(location)
            trim_done = True
            return location


if __name__ == "__main__":
    test_se_trouve = """Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?"""

    test_adresse_de = """Bonsoir Grandpy, j'espère que tu as passé une belle semaine. Est-ce que tu pourrais m'indiquer l'adresse de la tour eiffel? Merci d'avance et salutations à Mamie."""

    test_pas_adresse = "se trouve la tour eiffel"
    # test1 = parse(test_se_trouve)
    # test2 = parse(test_adresse_de)
    test3 = parse(test_pas_adresse)
    # trim_article_location(test1)
    # trim_article_location(test2)
    trim_article_location(test3)
