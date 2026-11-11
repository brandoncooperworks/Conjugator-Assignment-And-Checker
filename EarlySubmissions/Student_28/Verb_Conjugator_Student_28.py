
def conjug(pronoun, verb):
    pronoun = pronoun.lower()
    verb = verb.lower()
    verbending = verb[-2:]
    verbstem = verb[:-2]
    newWord = ""

    if pronoun == "yo":
        newWord = verbstem + "o"

    if pronoun == "tu":
        if verbending == "ar":
            newWord = verbstem + "as"
        elif verbending == "er" or "ir":
            newWord = verbstem + "es"

    if pronoun == "nosotros":
        if verbending == "ar":
            newWord = verbstem + "amos"
        elif verbending == "er":
            newWord = verbstem + "emos"
        elif verbending == "ir":
            newWord = verbstem + "imos"

    if pronoun == "el" or pronoun == "ella" or pronoun == "usted":
        if verbending == "ar":
            newWord = verbstem + "a"
        elif verbending == "er" or verbending == "ir":
            newWord = verbstem + "e"

    if pronoun == "ellos" or pronoun == "ellas" or pronoun == "ustedes":
        if verbending == "ar":
            newWord = verbstem + "an"
        if verbending == "er" or verbending == "ir":
            newWord = verbstem + "en"

    return pronoun + " " + newWord


