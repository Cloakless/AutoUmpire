import os
from running import *
from assassin_class import *

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
        data = {name: load_file, settings: game_config, players: player_list}
    main_operation(data)

def newgame():
    game_config = {}
    game_config['umpire_name'] = input("What is your name? ")
    game_name = input("Please input the name of the new game, eg 'Mich-15,txt' or 'Lent-19.txt': ")
    player_list = []
    print("Begin adding players now.")
    player_list = add_more_players(player_list)
    print("Welcome, umpire.")
    data = {'name': game_name, 'settings': game_config, 'players': player_list}
    save(data)
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

    loaded_data = {'name': file, 'settings': game_config, 'players': player_list}
    return loaded_data
    

def save(data):
    with open(data['name'], 'w') as file:
        config = data['settings']
        file.write(str(config)+'\n')
        list_of_players = []
        for assassin in data['players']:
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
        new_assassin = {'name': name, 'email': email, 'college': college, 'address': address, 'waterStatus': waterStatus, 'pseudonym': [pseudonym], 'notes': notes, 'isPolice': isPolice, 'isAlive': True, 'policeRank': rank, 'isWanted': False}
        return Assassin(new_assassin)
    else:
        return False


def unpack(assassin):
    details = {}
    details['name'] = assassin.name
    details['email'] = assassin.email
    details['college'] = assassin.college
    details['address'] = assassin.address
    details['waterStatus'] = assassin.waterStatus
    details['pseudonym'] = assassin.pseudonym
    details['notes'] = assassin.notes
    details['isPolice'] = assassin.isPolice
    details['isAlive'] = assassin.isAlive
    details['policeRank'] = assassin.policeRank
    details['isWanted'] = assassin.isWanted
    return details
    



def repack(details):
    '''
    name = details['name']
    email = details['email']
    college = details['college']
    address = details['address']
    waterStatus = details['waterStatus']
    pseudonym = details['pseudonym']
    notes = details['notes']
    isPolice = details['isPolice']
    isAlive = details['isAlive']
    policeRank = details['policeRank']
    isWanted = details['isWanted']
    loaded_assassin = [name, email, college, address, waterStatus, pseudonym, notes, isPolice, isAlive, policeRank, isWanted]
    '''
    return Assassin(details)

#test comment
#another test commit
