
def question_input(display_sentence):
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


number_people = question_input("Number of people in your event : ")
number_women = question_input("Number of women in your event : ")
number_men = question_input("Number of men in your event : ")
number_boy = question_input('Number of little boys in your event ')

