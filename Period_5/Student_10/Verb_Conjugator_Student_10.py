
def Conjug(pronoun, verb):
    newWord = ""
    if pronoun == "yo" or pronoun == "Yo":
        if (verb[-2: ]) == "ar" or (verb[-2: ]) == "er" or (verb[-2: ]) == "ir":
            end = verb.index(verb[-2: ])
            stem =(verb[0:end])
            newWord = (stem + "o")

    if pronoun == "tu" or pronoun == "Tu":
        if (verb[-2:]) == "ar":
            end = verb.index(verb[-2:])
            stem = (verb[0:end])
            newWord = (stem + "as")

        if (verb[-2:]) == "er" or (verb[-2:]) == "ir":
            end = verb.index(verb[-2:])
            stem = (verb[0:end])
            newWord = (stem + "es")

    if pronoun == "nosotros" or pronoun == "Nosotros":
        if (verb[-2:]) == "ar":
            end = verb.index(verb[-2:])
            stem = (verb[0:end])
            newWord = (stem + "amos")

        if (verb[-2:]) == "er":
            end = verb.index(verb[-2:])
            stem = (verb[0:end])
            newWord = (stem + "emos")

        if (verb[-2:]) == "ir":
            end = verb.index(verb[-2:])
            stem = (verb[0:end])
            newWord = (stem + "imos")

    if pronoun == "el" or pronoun == "ella" or pronoun == "usted" or pronoun == "El" or pronoun == "Ella" or pronoun == "Usted":
        if (verb[-2:]) == "ar":
            end = verb.index(verb[-2:])
            stem = (verb[0:end])
            newWord = (stem + "a")

        if (verb[-2:]) == "er" or (verb[-2:]) == "ir":
            end = verb.index(verb[-2:])
            stem = (verb[0:end])
            newWord = (stem + "e")

    if pronoun == "ellos" or pronoun == "ellas" or pronoun == "ustedes" or pronoun == "Ellos" or pronoun == "Ellas" or pronoun == "Ustedes":
        if (verb[-2:]) == "ar":
            end = verb.index(verb[-2:])
            stem = (verb[0:end])
            newWord = (stem + "an")

        if (verb[-2:]) == "er" or (verb[-2:]) == "ir":
            end = verb.index(verb[-2:])
            stem = (verb[0:end])
            newWord = (stem + "en")
    print(pronoun, newWord)
    return

