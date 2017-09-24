from setup import *
from assassin_class import *

def main_menu(data):
    game_name = data['name']
    game_config = data['settings']
    player_list = data['players']
    print('Main Menu:')
    print(game_name)
    print(game_config)
    print(player_list)
    print(player_list[0].name)
    player_menu(data)


def player_menu(data):
    while True:
        option = input('Add new player: n\n Edit an existing player: e\n')
        if option == 'n':
            data['players'] = add_more_players(data['players'])
            break
