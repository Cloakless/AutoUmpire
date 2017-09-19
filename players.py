class Assassin(object):
    def __init__(self, name, email, college, address, waterStatus, pseudonym, notes, isPolice, isAlive, policeRank, isWanted):
        self.name = name
        self.email = email
        self.college = college
        self.address = address
        self.waterStatus = waterStatus
        self.pseudonym = pseudonym
        self.notes = notes
        self.isPolice = bool(isPolice)
        self.isAlive = bool(isAlive)
        self.policeRank = int(policeRank)
        self.isWanted = bool(isWanted)
