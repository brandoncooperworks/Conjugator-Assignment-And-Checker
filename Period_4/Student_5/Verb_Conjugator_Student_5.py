def conjug(pronoun,verb):
    pronoun = pronoun.capitalize()
    verb = verb.lower()
    word = ""
    verbstem = pronoun + " " + verb[:-2]
    end = verb[-2:]
    if pronoun == "Yo":
        verbend = "o"
        word += verbstem + verbend
    elif pronoun == "Tu":
        if end == "ar":
            verbend = "as"
            word += verbstem + verbend
        else:
            verbend = "es"
            word += verbstem + verbend
    elif pronoun == "Nosotros":
        if end == "ar":
            verbend = "amos"
            word += verbstem + verbend
        elif end == "er":
            verbend = "emos"
            word += verbstem + verbend
        elif end == "ir":
            verbend = "imos"
            word += verbstem + verbend
    elif pronoun == "El" or pronoun == "Ella" or pronoun == "Usted":
        if end == "ar":
            verbend = "a"
            word += verbstem + verbend
        elif end == "er" or end == "ir":
            verbend = "e"
            word += verbstem + verbend
    elif pronoun == "Ellos" or pronoun == "Ellas" or pronoun == "Ustedes":
        if end == "ar":
            verbend = "an"
            word += verbstem + verbend
        elif end == "er" or end == "ir":
            verbend = "en"
            word += verbstem + verbend
    return word
