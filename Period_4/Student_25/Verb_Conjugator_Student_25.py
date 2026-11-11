def conjugate(verb, pronoun):
    pronoun = pronoun.lower()
    stem = verb[:-2]
    stem = stem.lower()
    ending = verb[-2:]
    ending = ending.lower()
    word = " "
    word = word.lower()
    if pronoun == "yo":
        word = stem + "o"
    elif pronoun == "tu":
        if ending == "ar":
            word = stem + "as"
        else:
            word = stem + "es"
    elif pronoun == "nosotros":
        word = verb[:-1] + "mos"

    elif pronoun == "usted" or pronoun == "el" or pronoun == "ella":
        if ending == "ar":
            word = stem + "a"
        else:
            word = stem + "e"
    elif pronoun == "ustedes" or pronoun == "ellos" or pronoun == "ellas":
        if ending == "ar":
            word = stem + "an"
        else:
            word = stem + "en"
    return pronoun + " " + word.lower()
