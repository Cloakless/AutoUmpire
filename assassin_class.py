from email_sending import send_email

class Assassin(object):
    def __init__(self, information):
        self.name = information['name']
        self.email = information['email']
        self.college = information['college']
        self.address = information['address']
        self.waterStatus = information['waterStatus']
        self.pseudonym = information['pseudonym']
        self.notes = information['notes']
        self.isPolice = bool(information['isPolice'])
        self.isAlive = bool(information['isAlive'])
        self.policeRank = int(information['policeRank'])
        self.isWanted = bool(information['isWanted'])
        self.playerID = int(information['playerID'])


def add_more_players(player_list):
    while True:
        new_player = add_player(len(player_list)+1)
        if new_player != False:
            player_list.append(new_player)
            test = input("Player successfully added. Press enter to continue adding players, or any other key to proceed to other options. ")
            if test != '':
                return player_list

def add_player(playerID):
    name = input("Name? ")
    college = input("College? ")
    address = input("Address/Room number? ")
    email = input("CRSId or email? ")
    if '@' not in email:
        email += '@cam.ac.uk'
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
        new_assassin = {'name': name, 'email': email, 'playerID': playerID, 'college': college, 'address': address, 'waterStatus': waterStatus, 'pseudonym': [pseudonym], 'notes': notes, 'isPolice': isPolice, 'isAlive': True, 'policeRank': rank, 'isWanted': False}
        return Assassin(new_assassin)
    else:
        return False


def save(data):
    with open(data['name'], 'w') as file:
        config = data['settings']
        file.write(str(config)+'\n')
        list_of_players = []
        for assassin in data['players']:
            list_of_players.append(unpack(assassin))
        file.write(str(list_of_players))
        file.write(str(data['events']))

def load(file):
    player_list = []
    with open(file, 'r') as load_file:
        config_string = (load_file.readline()).strip()
        game_config = eval(config_string)
        list_of_players = eval((load_file.readline()).strip())
        for details in list_of_players:
            player_list.append(repack(details))
        event_list = eval((load_file.readline()).strip())
    loaded_data = {'name': file, 'settings': game_config, 'players': player_list, 'events': event_list}
    return loaded_data

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
    return Assassin(details)
