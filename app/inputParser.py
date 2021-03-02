
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
    importantWordBefore = ["adresse de", "se trouve", "se situe" "est situé"]
    importantWordAfter = ["?", ",", "."]
    for beforeWord in importantWordBefore:
        if beforeWord in stringToParse:
            breakWordLength = len(beforeWord)
            startIndex = stringToParse.find(beforeWord)+breakWordLength
            parsedString = stringToParse[startIndex:length+1]
            for afterWord in importantWordAfter:
                while parsing_done == False:
                    if afterWord in parsedString:
                        endIndex = parsedString.find(afterWord)
                        parsedString = parsedString[0:endIndex]
                        parsing_done = True
            return parsedString
        else:
            return "Tu es sûr qu'il y a un lieu dans ta question?"

        print(parsedString)


def trim_article_location(location):
    """
    Remove article in the location like "la" in "la tour eiffel"
    """
    articles = ["la ", "le ", "les ", "l'"]
    for article in articles:
        if article in location[:3]:
            location = location[:3].replace(article, '')+location[3:]
    print(location)
    return location


if __name__ == "__main__":
    test_se_trouve = """Salut grandpy! 
    Comment s'est passé ta soirée avec Grandma hier soir?
    Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve
    le musée d'art et d'histoire de Fribourg, s'il te plaît?"""

    test_adresse_de = """Bonsoir Grandpy, j'espère que tu as passé une belle semaine. 
    Est-ce que tu pourrais m'indiquer l'adresse de la tour eiffel? 
    Merci d'avance et salutations à Mamie."""

    parse(test_se_trouve)
    parse(test_adresse_de)
    trim_article_location("la tour Eiffel")
