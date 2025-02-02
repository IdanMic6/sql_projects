from person_class import Person
from utils import getOnlyNumber

class Employee(Person):
    def __init__(self, id_number, name, age):
        super().__init__(id_number, name, age)
        self.job_title = input("What is your job title? ")
        self.salary = getOnlyNumber("salary")  

    def getInfoDict(self):
        person_info = super().getInfoDict()
        person_info.update({
            "job_title": self.job_title,
            "salary": self.salary
        })
        return person_info

    def printInfo(self):
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("ID: " + self.id_number)
        print("Job Title: " + self.job_title)
        print("Salary: " + str(self.salary))
