from variable import explanation_russian_roulette
from function_usefull import number_input 
from function_usefull import bool_input
from random import randrange
from time import sleep
lightsaber = 2
revolver = 6
ak47 = 30

def print_suspense():
    text = [['1','.','.','.'],['2','.','.','.'],['3','.','.','.'],['FIRE !']]
    for list in text:
        for char in list:
            print(char, end='')
            sleep(0.1)
        print('\n')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def game(players, kill_bullet,ammo):
    perdant = ''
    complete = False
    bullet = 1
    while not complete:
        _ = input("Enter to continue:")
        print_suspense()
        player_turn = players[0]
        if bullet == kill_bullet:
            perdant = player_turn
            complete
            return perdant
        print(f"The player {player_turn} it's not dead (stay {ammo - bullet})")
        players.append(players.pop(0))
        bullet += 1
        if bullet > 30:
            print("the weapon is jammed")
            return "Gun", 0
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def game_ak47(players, kill_bullet):
    perdant = ''
    complete = False
    bullet = 0
    while not complete:
        _ = input("Enter to continue:")
        number_bullet = 1
        player_turn = players[0]
        if player_turn == 'user':
            burst = bool_input("Do you want to use the burst mod ? :")
            if burst :
                number_bullet = 3
        else:
            burst = randrange(0,2)
            if burst == 1:
                number_bullet = 3
        print_suspense()
        for _ in range(number_bullet):
            bullet += 1
            if bullet == kill_bullet:
                perdant = player_turn
                complete
                return perdant
        print(f"The player {player_turn} it's not dead (stay {30 - bullet})")
        if bullet > 30:
            print("the weapon is jammed")
            return "Gun", 0
        players.append(players.pop(0))
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def russian_roulette():
    print(explanation_russian_roulette)

    input_ammo = input("Choose between lightsaber, revolver and ak47 :")
    while input_ammo not in ["lightsaber", "revolver", "ak47"]:
        print('_' * 50 + '\n' + 'Not valid !')
        input_ammo = input("Choose between lightsaber, revolver and ak47 :")
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ammo = 0
    if input_ammo == "lightsaber":
        ammo = lightsaber
    elif input_ammo == "revolver":
        ammo = revolver
    elif input_ammo == "ak47":
        ammo = ak47
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    input_bot = int(number_input("Choose the number of bot : "))
    players = ['user']
    for i in range(input_bot):
        name = 'bot' + str(i+1)
        players.append(name)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    kill_bullet = randrange(1,ammo + 1)
    perdant = ''
    if input_ammo != 'ak47':
        perdant = game(players, kill_bullet, ammo)
    elif input_ammo == 'ak47':
        perdant = game_ak47(players, kill_bullet)

    print(f"The player {perdant} is dead with the bullet number {kill_bullet}")
