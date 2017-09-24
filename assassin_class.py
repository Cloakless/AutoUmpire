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
