def conjug(x,y):
    ns = ""
    x=x.lower()
    y=y.lower()
    end = y[-2]
    stem = y[0:-2]
    stem2 = y[0:-1]
    if x == "el" or x == "ella" or x == "usted":
        if end == "a":
            ns += stem
            ns += "a"
        if end == "e" or end=="i":
            ns += stem
            ns += "e"
    elif x == "yo" or x== "Yo":
        if end == "a" or end == "e" or end=="i":
            ns += stem
            ns += "o"
    elif x == "tu" or x=="Tu":
        if end== "a":
            ns += stem
            ns += "as"
        if end == "e" or end=="i":
            ns += stem
            ns += "es"
    elif x =="nosotros" or x=="Nosotros":
        if end== "a" or end== "i" or end== "e":
            ns += stem2
            ns += "mos"
    elif x == "ustedes" or x == "ellos" or x == "ellas":
        if end == "a":
            ns += stem
            ns += "an"
        if end == "e" or end=="i":
            ns += stem
            ns += "en"
    return x+ " "+ ns
