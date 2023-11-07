from kiss import kiss
from philipe_unit import philipe
from function_usefull import *

txt_user_enter = "User say : "
DICO_FUNCTION = {"description" : description,
                  "kiss" : kiss,
                  "philipe" : philipe,
                  "exit" : None}

print(f"Welcome to Bricabrac !")
operating = True
while operating:
    print(f"Enter the function you want to execute :{list(DICO_FUNCTION.keys())} :")
    user_input = input(txt_user_enter)
    while user_input not in DICO_FUNCTION:
        print("_" * 50  + "\n"+ "Not valid ! ")
        print(f"Enter the function you want to execute :{list(DICO_FUNCTION.keys())} :")
        user_input = input(txt_user_enter)
    print('_'* 50)
    if user_input == "exit":
        break
    DICO_FUNCTION[user_input]()

