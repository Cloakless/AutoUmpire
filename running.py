from setup import *
from players import *

def main_operation(data):
    game_name = data[0]
    game_config = data[1]
    player_list = data[2]
    print("Entering main operation...")
    print(game_name)
    print(game_config)
    print(player_list)
    print(player_list[0].name)
