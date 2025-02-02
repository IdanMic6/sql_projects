from person_class import Person
from utils import getOnlyNumber

class Student(Person):
    def __init__(self, id_number, name, age):
        super().__init__(id_number, name, age)
        self.field_of_study = input("What are you studying?")
        self.year_of_study = getOnlyNumber("year of study")  
        self.score_avg = getOnlyNumber("average score")  

    def getInfoDict(self):
        person_info = super().getInfoDict()  
        person_info.update({
            "field_of_study": self.field_of_study,
            "year_of_study": self.year_of_study,
            "score_avg": self.score_avg
        })
        return person_info

    def printInfo(self):
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("ID: " + self.id_number)
        print("Field of Study: " + self.field_of_study)
        print("Year of Study: " + str(self.year_of_study))
        print("Average Score: " + str(self.score_avg))
