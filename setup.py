import os
from running import *
from players import *

def startup():
    print("Welcome to the Cambridge Assassins' Guild AutoUmpire.")
    while True:
        start_path = input("To begin a new game, press 'n'. To load a previous game, press 'p'. ")
        if start_path == 'n' or start_path == 'p':
            break
        print("Invalid option. ", end = "")
    if start_path == 'n':
        data = newgame()
    else:
        while True:
            load_file = input("Please enter the name of the game you wish to load. ")
            if not os.path.isfile('./' + load_file):
                print("That is not a valid file name. ", end = "")
            else:
                print("Loading " + load_file + " ...")
                loaded_data = load(load_file)
                game_config = loaded_data[0]
                player_list = loaded_data[1]
                break
        data = [load_file, game_config, player_list]
    main_operation(data)

def newgame():
    game_config = {}
    game_config['umpire_name'] = input("What is your name? ")
    game_name = input("Please input the name of the new game, eg 'Mich-15,txt' or 'Lent-19.txt': ")
    player_list = []
    print("Begin adding players now.")
    player_list = add_more_players(player_list)
    print("Welcome, umpire.")
    save(game_name, game_config, player_list)
    data = [game_name, game_config, player_list]
    return data

def add_more_players(player_list):
    while True:
        new_player = add_player()
        if new_player != False:
            player_list.append(new_player)
            test = input("Player successfully added. Press enter to continue adding players, or any other key to proceed to other options. ")
            if test != '':
                return player_list

def load(file):
    player_list = []
    with open(file, 'r') as load_file:
        config_string = (load_file.readline()).strip()
        game_config = eval(config_string)
        list_of_players = eval((load_file.readline()).strip())
        for details in list_of_players:
            player_list.append(repack(details))

    loaded_data = [game_config, player_list]
    return loaded_data
    

def save(file_name, config, player_list):
    with open(file_name, 'w') as file:
        saved_dict = config
        file.write(str(saved_dict)+'\n')
        list_of_players = []
        for assassin in player_list:
            list_of_players.append(unpack(assassin))
        file.write(str(list_of_players))


def add_player():
    name = input("Name? ")
    college = input("College? ")
    address = input("Address/Room number? ")
    email = input("CRSId or email? ")
    while True:
        water = input("Water status? ('n' for No Water, 'c' for Water With Care, 'f' for Full Water) ")
        if (water == 'n') or (water == 'c') or (water == 'f'):
            if water == 'n':
                waterStatus = 'No Water'
            elif water == 'c':
                waterStatus = 'Water With Care'
            else:
                waterStatus = 'Full Water'
            break
        else:
            print("Invalid water status. Please try again.")
    pseudonym = input("Initial pseudonym? ")
    notes = input("Notes? ")
    while True:
        police = input("Police? (y/n) ")
        if (police == 'y'):
            isPolice = True
            rank = input("Police rank? Default is 1, resurrected players are 0. ")
            break
        elif (police == 'n'):
            isPolice = False
            rank = 0
            break
        else:
            print("Invalid answer. Please try again. ", end = '')
    print("You are about to add %s, of %s, %s, email %s with an initial pseudonym of %s, police status: %s and additional notes: %s" % (name, address, college, email, pseudonym, isPolice, notes))
    confirmation = input("Press enter to confirm; to cancel enter any other string. ")
    if confirmation == '':
        new_assassin = [name, email, college, address, waterStatus, [pseudonym], notes, isPolice, True, rank, False]
        return Assassin(*new_assassin)
    else:
        return False


def unpack(assassin):
    details = []
    details.append(assassin.name)
    details.append(assassin.email)
    details.append(assassin.college)
    details.append(assassin.address)
    details.append(assassin.waterStatus)
    details.append(assassin.pseudonym)
    details.append(assassin.notes)
    details.append(assassin.isPolice)
    details.append(assassin.isAlive)
    details.append(assassin.policeRank)
    details.append(assassin.isWanted)
    return details
    



def repack(details):
    name = details[0]
    email = details[1]
    college = details[2]
    address = details[3]
    waterStatus = details[4]
    pseudonym = details[5]
    notes = details[6]
    isPolice = details[7]
    isAlive = details[8]
    policeRank = details[9]
    isWanted = details[10]
    loaded_assassin = [name, email, college, address, waterStatus, pseudonym, notes, isPolice, isAlive, policeRank, isWanted]
    return Assassin(*loaded_assassin)

#test comment
#another test commit
