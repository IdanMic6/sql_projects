class Person:
    def __init__(self, id_number, name, age):
        self.id_number = id_number
        self.name = name
        self.age = age
    
    def getInfoDict(self):
        return {
            "id": self.id_number,
            "name": self.name,
            "age": self.age
        }

    def printInfo(self):
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("ID: " + self.id_number)
