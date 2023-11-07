from philipe_unit import explanation_philipe
from kiss import explanation_kiss



def number_input(display_sentence):
        entrer = input(display_sentence)
        valid = False
        try:
            entrer = int(entrer)
            valid = True
        except:
            valid = False
        while not valid:
            print("_" * 50  + "\n"+ "Not valid ! ")
            entrer = input(display_sentence)
            try :
                entrer =int(entrer)
                valid = True
            except:
                valid = False 
        return entrer

def description():
     pass