import math
def kiss():
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
    number_kiss = abs(question_input("Number of kiss you do with one person : "))

    if number_kiss == 0:
        number_men += number_women + number_boy
        number_women = 0
        number_boy = 0

    number_people = number_women + number_men + number_boy
    interation = math.comb(number_people, 2)
    number_total_kiss =  (number_women+ number_boy) * (number_people-1) * number_kiss 
    number_total_handshake = math.comb(number_men,2)

    print('~' * 50)
    print(f"""In your event, for a total of {number_people} peoples, \n
    the number of kisses is {number_total_kiss}, \n
    the number of handshake is {number_total_handshake},\n
    the number of possibilities for transmitting the disease is {interation}.""")
