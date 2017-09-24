from setup import *
from assassin_class import *

def main_menu(data):
    while True:
        game_name = data['name']
        game_config = data['settings']
        player_list = data['players']
        menu_selection = input('\nMAIN MENU\n\nPlayer Menu: p\nEvent Menu: e\nGame Menu: g\nWebsite Menu: w\nSave and Exit: x\n')

        data = player_menu(data)


def player_menu(data):
    while True:
        option = input('\nPLAYER MENU\n\nAdd new player: n\nEdit an existing player: e\nReturn to Main Menu: x\n')
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

def event_menu(data):
    while True:
        option = input('\nEVENT MENU\n\nEvent options\n')
        #event menu
    return data

def game_menu(data):
    #game actions
    return data

def website_menu(data):
    #website stuff
    return data
