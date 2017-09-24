from setup import *
from assassin_class import *

def main_operation(data):
    game_name = data['name']
    game_config = data['settings']
    player_list = data['players']
    print("Entering main operation...")
    print(game_name)
    print(game_config)
    print(player_list)
    print(player_list[0].name)


def player_menu(data):
    while True:
        option = input('To add a new player, press n. To edit an existing player, press e. ')
        break
