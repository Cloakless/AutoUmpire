from setup import *
from assassin_class import *

def main_menu(data):
    while True:
        option = input('\nMAIN MENU\n\nPlayer Menu: p\nEvent Menu: e\nGame Menu: g\nWebsite Menu: w\nSave and EXIT: x\n')
        if option == 'p':
            data = player_menu(data)
        elif option == 'e':
            data = event_menu(data)
        elif option == 'g':
            data = game_menu(data)
        elif option == 'w':
            data = website_menu(data)
        elif option == 'x':
            save(data)
            break
        else:
            print('Invalid selection. Please select another option.\n')


def player_menu(data):
    while True:
        option = input('\nPLAYER MENU\n\nAdd new player: n\nEdit an existing player: e\nReturn to Main Menu: x\n')
        if option == 'n':
            data['players'] = add_more_players(data['players'])
            print('\nPlayers added successfully\n')
        elif option == 'e':
            #edit existing player
            break
        elif option == 'x':
            break
        else:
            print('Invalid selection. Please select another option.\n')
    return data

def event_menu(data):
    #event stuff
    while True:
        option = input('\nEVENT MENU\n\nEVENT OPTIONS\nReturn to Main Menu: x\n')
        if option == 'n':
            data['players'] = add_more_players(data['players'])
            break
        elif option == 'e':
            #edit existing player
            break
        elif option == 'x':
            break
        else:
            print('Invalid selection. Please select another option.\n')
    return data

def game_menu(data):
    #game stuff
    while True:
        option = input('\nGAME MENU\n\nGAME OPTIONS\nReturn to Main Menu: x\n')
        if option == 'n':
            data['players'] = add_more_players(data['players'])
            break
        elif option == 'e':
            #edit existing player
            break
        elif option == 'x':
            break
        else:
            print('Invalid selection. Please select another option.\n')
    return data

def website_menu(data):
    #website stuff
    while True:
        option = input('\nWEBSITE MENU\n\nWEBSITE OPTIONS\nReturn to Main Menu: x\n')
        if option == 'n':
            data['players'] = add_more_players(data['players'])
            break
        elif option == 'e':
            #edit existing player
            break
        elif option == 'x':
            break
        else:
            print('Invalid selection. Please select another option.\n')
    return data
