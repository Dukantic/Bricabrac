from kiss import kiss

txt_user_enter = "User say : "
LISTE_FONCTION = {"kiss" : kiss,
                  "test" : "bla"}

print(f"Welcome to Bricabrac, enter the function you want to execute :{list(LISTE_FONCTION.keys())} :")
user_input = input(txt_user_enter)
while user_input not in LISTE_FONCTION:
    print("_" * 50  + "\n"+ "Not valid ! ")
    print(f"Enter the function you want to execute :{list(LISTE_FONCTION.keys())} :")
    user_input = input(txt_user_enter)
print('_'* 50)
LISTE_FONCTION[user_input]()