
def question_input(phrase_affiche):
    entrer = input(phrase_affiche)
    valide = False
    try:
        entrer = int(entrer)
        valide = True
    except:
        valide = False
    while not valide:
        print("_" * 50  + "\n"+ "Entré pas bonne !")
        entrer = input(phrase_affiche)
        try :
            entrer =int(entrer)
            valide = True
        except:
            valide = False
    return entrer


