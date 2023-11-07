from variable import *

def number_input(display_sentence):
        entrer = input(display_sentence)
        valid = False
        try:
            entrer = float(entrer)
            valid = True
        except:
            valid = False
        while not valid:
            print("_" * 50  + "\n"+ "Not valid ! ")
            entrer = input(display_sentence)
            try :
                entrer =float(entrer)
                valid = True
            except:
                valid = False 
        return entrer

def description():
    for string in LISTE_EXPLANATION:
        print(string)
    