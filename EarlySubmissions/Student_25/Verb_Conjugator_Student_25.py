def conjug(pronoun, v):
    p = pronoun.lower()
    verb = v.lower()
    ending = verb[-2:]
    if p == "yo":
        verb = verb.replace(ending, "o")
    if p == "tu":
        if ending == "ar":
            verb = verb.replace(ending, "as")
        if ending == "er" or ending == "ir":
            verb = verb.replace(ending, "es")
    if p == "nosotros":
        if ending == "ar":
            verb = verb.replace(ending, "amos")
        if ending == "er":
            verb = verb.replace(ending, "emos")
        if ending == "ir":
            verb = verb.replace(ending, "imos")
    if p == "el" or p == "ella" or p == "usted":
        if ending == "ar":
            verb = verb.replace(ending, "a")
        if ending == "er" or ending == "ir":
            verb = verb.replace(ending, "e")
    if p == "ellos" or p == "ellas" or p == "ustedes":
        if ending == "ar":
            verb = verb.replace(ending, "an")
        if ending == "er" or ending == "ir":
            verb = verb.replace(ending, "en")
    return p + " " + verb

