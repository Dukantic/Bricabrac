from kiss import kiss
from philipe_unit import philipe
from function_usefull import *

txt_user_enter = "User say : "
LISTE_FONCTION = {"description" : description,
                  "kiss" : kiss,
                  "philipe" : philipe,
                  "exit" : None}

print(f"Welcome to Bricabrac, enter the function you want to execute :{list(LISTE_FONCTION.keys())} :")
operating = True
while operating:
    user_input = input(txt_user_enter)
    while user_input not in LISTE_FONCTION:
        print("_" * 50  + "\n"+ "Not valid ! ")
        print(f"Enter the function you want to execute :{list(LISTE_FONCTION.keys())} :")
        user_input = input(txt_user_enter)
    print('_'* 50)
    if user_input == "exit":
        break
    LISTE_FONCTION[user_input]()

