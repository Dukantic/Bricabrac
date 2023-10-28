
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


number_women = question_input("Number of women in your event : ")
number_men = question_input("Number of men in your event : ")
number_boy = question_input('Number of little boys in your event : ')
number_kiss = question_input("Number of kiss you do with one person : ")
number_people = number_women + number_men + number_boy



number_total_kiss = (number_people + number_boy) * (number_people-1) * number_kiss
number_total_handshake = number_men * (number_men - 1)

print(f"In your event, for a total of {number_people} peole, the number of kisses is {number_total_kiss}, the number of handshake is {number_total_handshake}.")