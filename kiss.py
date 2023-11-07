import math
from function_usefull import *
from variable import *

def kiss():
    print(explanation_kiss)

    number_women = number_input("Number of women in your event : ")
    number_men = number_input("Number of men in your event : ")
    number_boy = number_input('Number of little boys in your event : ')
    number_kiss = abs(number_input("Number of kiss you do with one person : "))

    if number_kiss == 0:
        number_men += number_women + number_boy
        number_women = 0
        number_boy = 0

    number_people = number_women + number_men + number_boy
    interation = math.comb(int(number_people), 2)
    number_total_kiss =  (number_women+ number_boy) * (number_people-1) * number_kiss 
    number_total_handshake = math.comb(int(number_men),2)

    print('~' * 50)
    print(f"""In your event, for a total of {int(number_people)} peoples, \n
    the number of kisses is {int(number_total_kiss)}, \n
    the number of handshake is {int(number_total_handshake)},\n
    the number of possibilities for transmitting the disease is {int(interation)}.""")