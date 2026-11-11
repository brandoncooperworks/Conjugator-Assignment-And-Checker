def changeletter_thing(pronoun,verb):
    pronoun = pronoun.lower()
    verb = verb.lower()
    verb_ending = verb[-2:]
    verb_stem = verb[:-2]
    new_word = ""
    if (pronoun == "yo"):
        new_word = verb_stem + "o"
    elif(pronoun == "tu"):
        if (verb_ending == "ar"):
            new_word = verb_stem + "as"
        else:
            new_word = verb_stem + "es"
    elif(pronoun == "nosotros"):
        if (verb_ending == "ar"):
            new_word = verb_stem + "amos"
        elif (verb_ending == "er"):
            new_word = verb_stem + "emos"
        elif (verb_ending == "ir"):
            new_word = verb_stem + "imos"
    elif(pronoun == "el") or (pronoun == "ella") or (pronoun == "usted"):
        if (verb_ending == "ar"):
            new_word = verb_stem + "a"
        else:
            new_word = verb_stem + "e"
    elif(pronoun == "ellos") or (pronoun == "ellas") or (pronoun == "ustedes"):
        if (verb_ending == "ar"):
            new_word = verb_stem + "an"
        else:
            new_word = verb_stem + "en"
    phrase = pronoun + " " + new_word
    return phrase


