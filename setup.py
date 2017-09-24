import os
from menus import *
from assassin_class import *

def startup():
    print('Welcome to the Cambridge Assassins\' Guild AutoUmpire.')
    while True:
        start_path = input('To begin a new game, press \'n\'. To load a previous game, press \'p\'. ')
        if start_path == 'n' or start_path == 'p':
            break
        print('Invalid option. ', end = '')
    if start_path == 'n':
        data = newgame()
    else:
        while True:
            load_file = input('Please enter the name of the game you wish to load. ')
            if not os.path.isfile('./' + load_file):
                print('That is not a valid file name. ', end = '')
            else:
                print('\nLoading ' + load_file + ' ...')
                loaded_data = load(load_file)
                print('Loaded game succesfully.\n')
                break
        data = loaded_data
    print('\nWelcome, ' + data['settings']['umpire_name'])
    main_menu(data)

def newgame():
    game_config = {}
    game_config['umpire_name'] = input('What is your name? ')
    game_name = input('Please input the name of the new game, eg \'Mich-15,txt\' or \'Lent-19.txt\': ')
    player_list = []
    print('Begin adding players now.')
    player_list = add_more_players(player_list)
    print('Welcome, umpire.')
    data = {'name': game_name, 'settings': game_config, 'players': player_list, 'events': []}
    save(data)
    return data
