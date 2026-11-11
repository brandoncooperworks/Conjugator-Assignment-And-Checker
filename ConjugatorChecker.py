import os, re, sys, time
from pathlib import Path

Twords = 0
Tlines = 0
TcharCount = 0
Tspaces = 0
TnonSpaceChars = 0
numStudents = 0

def conjugate2(pro, verb):
    pro = pro.lower()
    verb = verb.lower()
    stem = verb[:-2]
    ending = verb[-2:]
    conWord = ""     # Conjugated Word initalization

    if(pro == "yo"):
        conWord = stem + "o"
    elif(pro == "tu"):
        if(ending == "ar"):conWord = stem + "as"
        elif(ending == "er" or ending == "ir"): conWord = stem + "es"

    elif(pro == "nosotros"): stem = verb[:-1]; conWord = stem + "mos"
    elif(pro == "el" or pro == "ella" or pro == "usted" ):
        if(ending == "ar"): conWord = stem + "a"
        elif(ending == "er" or ending == "ir"): conWord = stem + "e"

    elif(pro == "ellos" or pro == "ellas" or pro=="ustedes"):
        if(ending == "ar"): conWord = stem + "an"
        elif(ending == "er" or ending == "ir"): conWord = stem + "en"

    else: return "Invalid Verb"

    phrase = pro + " " + conWord
    return phrase


def checkList(functionName):
    pronouns = ["usTEdes", "ellA", "nosoTros",  "tu", "yO", ]
    print(Path.cwd())
    file = open("../../../Conjugator/regVerbs", "r")
    verblist = file.read().splitlines()
    file.close()

    numCorrect = 0
    for verb in verblist:
        #time.sleep(.25)
        print(verb.upper()+": -"+verb.upper()[-2:])
        for pronoun in pronouns:
            p, v = pronoun.title().swapcase(), verb.title().swapcase()
            output = eval(functionName+"("+"'"+p+"', '"+v+"')").lower()
            key = conjugate2(p,v)
            print(output, end = "\t")
            if output == key:
                print("Correct")
                numCorrect += 1
            else:
                print("INCORRECT")


        print()

    checks = len(verblist)*len(pronouns)
    pCorrect = round(numCorrect*100/checks,2)
    print("\n\nOutput Check: "+ str(pCorrect)+"%\nNum Correct: "+str(numCorrect)+"/"+str(checks)+"\n")

def fileStats(program):
    global Twords
    global Tlines
    global TcharCount
    global Tspaces
    global TnonSpaceChars
    global numStudents

    words = len(file.split())
    lines = len(file.splitlines())+1
    charCount = len(file)
    spaces = file.count(" ")
    nonSpaceChars = len(file) - spaces

    Twords += words
    Tlines += lines
    TcharCount += charCount
    Tspaces += spaces
    TnonSpaceChars += nonSpaceChars
    numStudents += 1

    print("FILE STATS:")
    print("Line Count:", lines)
    print("Word Count:", words)
    print("Space Count:", spaces)
    print("Char Count:", charCount)
    print("Non-Space Count:", nonSpaceChars)

pathways = []
print(Path.cwd())

class_periods = []

for file in os.listdir():
    if os.path.isdir(file) and file not in [".idea", ".gitignore", ".git"]:
        class_periods.append(file)

print("Which folder would you like to open below?")
for i in range(len(class_periods)):
    print(str(i) + " - " +class_periods[i])

folderChoice = int(input())
print("\n\n")

classroomFolder = class_periods[folderChoice]
os.chdir(Path(Path.cwd(), classroomFolder))
print(Path.cwd())

# For each student directory, add the file pathway to a list
for student in os.listdir():
    path = Path(Path.cwd(), student)
    pathways.append(path)

