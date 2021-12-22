class Person:
    def __init__(self, name, address, phoneNumber = None):
        self.name = name
        self.address = address
        self.phoneNumber = phoneNumber

    def printPersonData(self):
        print(self.name)
        print(self.address)
        print(self.phoneNumber)

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName