
def parse_exple():
    # for test purpose
    return "OK"


def parse(stringToParse):
    length = len(stringToParse)
    importantWordBefore = ["adresse de", "se trouve", "se situe" "est situé"]
    importantWordAfter = ["?", ",", "."]
    for beforeWord in importantWordBefore:
        if beforeWord in stringToParse:
            breakWordLength = len(beforeWord)
            startIndex = stringToParse.find(beforeWord)+breakWordLength
            parsedString = stringToParse[startIndex:length+1]
    for afterWord in importantWordAfter:
        if afterWord in parsedString:
            endIndex = parsedString.find(afterWord)
            parsedString = parsedString[0:endIndex]
    print(parsedString)
    return parsedString


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
