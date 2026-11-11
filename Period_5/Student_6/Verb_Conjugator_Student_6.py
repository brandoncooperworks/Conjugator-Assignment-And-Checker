def conjug(pro, verb):
    pro = pro.lower()
    verb = verb.lower()
    words = ""
    if pro == "yo":
        vStem = verb[:-2]
        vEnd = "o"
        words += pro + " " + vStem + vEnd
    elif pro == "tu":
        vStem = verb[:-2]
        vEnd = verb[-2:]
        if vEnd == "ar":
            vEnd = "as"
            words += pro + " " + vStem + vEnd
        else:
            vEnd = "es"
            words += pro + " " + vStem + vEnd
    elif pro == "nosotros":
        vStem = verb[:-2]
        vEnd = verb[-2:]
        if vEnd == "ar":
            vEnd = "amos"
            words += pro + " " + vStem + vEnd
        elif vEnd == "er":
            vEnd = "emos"
            words += pro + " " + vStem + vEnd
        else:
            vEnd = "imos"
            words += pro + " " + vStem + vEnd
    elif pro == "el" or pro == "ella" or pro == "usted":
        vStem = verb[:-2]
        vEnd = verb[-2:]
        if vEnd == "ar":
            vEnd = "a"
            words += pro + " " + vStem + vEnd
        else:
            vEnd = "e"
            words += pro + " " + vStem + vEnd
    else:
        vStem = verb[:-2]
        vEnd = verb[-2:]
        if vEnd == "ar":
            vEnd = "an"
            words += pro + " " + vStem + vEnd
        else:
            vEnd = "en"
            words += pro + " " + vStem + vEnd
    return words