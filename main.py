#import models
import pandas as pd
from person_class import Person
from student_class import Student
from employee_class import Employee
from utils import getOnlyNumber
from class_enum import Func

def saveToCSV(people):
  try:
    #create list for all the people details
    data = []
    for person in people.values():
        person_info = person.getInfoDict()
        data.append(person_info)
    df = pd.DataFrame(data)
    df.to_csv("/Users/idanmic/Desktop/Big project/people_info.csv", index=False)
  except Exception as e:
    print("Error saving to CSV, the error is:" + str(e))

#adding a new person to dict by user input
def addPerson(people_dict, age_avg_dict):
 try:
    name = input("Please enter name: ")  
    age = getOnlyNumber("age: ")  
    id_number = getOnlyNumber("ID number: ") 

    if str(id_number) in people_dict:
        print("Error: This ID number already exists. Please enter another ID.")
        return

    print("Select person type:")
    #A list containing all the options for types of people
    person_types = [Student, Employee, Person]
    for index, person_type in enumerate(person_types):
        print(str(index) + ". " + person_type.__name__)

    menu_choice_enum = getOnlyNumber("your choice (0-2): ")  

    if menu_choice_enum < 0 or menu_choice_enum >= len(person_types):
        print("Invalid choice.")
        return

    chosen_person_type = person_types[menu_choice_enum]
    person = chosen_person_type(str(id_number), name, age)
    people_dict[str(id_number)] = person
    age_avg_dict["age"] += age
    print("The last person was added successfully.")
 except Exception as e:
    print("Error adding person, the error is:" + str(e))

def printPersonInfo(person):
    try:
        person.printInfo()
    except Exception as e:
        print("Error printing person info, the error is" + str(e))

def checkEmpty(people):
    if len(people) == 0:
        print("No data available.")
        return True
    return False

def findByID(people):
    try:
        id_number = getOnlyNumber("Please enter ID number: ") 
        if str(id_number) in people:
            people[str(id_number)].printInfo()
        else:
            print("ID number not found.")
    except Exception as e:
        print("Error finding person by ID, the error is:" + str(e))

def printAllPersons(people):
    try:
        for person in people.values():
            person.printInfo()
    except Exception as e:
        print("Error printing all persons, the error is: " + str(e))

def printNames(people):
    if checkEmpty(people):
        return
    try:
        for index, person in enumerate(people.values()):
            print("Index: " + str(index) + " - Name: " + person.name)
    except Exception as e:
        print("Error printing names, the error is: " + str(e)) 

def printIDs(people):
    if checkEmpty(people):
        return
    try:
        for index, person in enumerate(people.values()):
            print("Index: " + str(index) + " - ID: " + str(person.id_number))
    except Exception as e:
        print("Error printing IDs, the error is: " +  str(e))

def personByIndex(people):
    if checkEmpty(people):
        return
    try:
        index = getOnlyNumber("Enter index: ")   
        if index < 0 or index >= len(people):
            print("Error: Invalid index.")
            return
        person = list(people.values())[index]
        printPersonInfo(person)
    except Exception as e:
        print("Error retrieving person by index, the error is" + str(e))

def printInvalidChoice():
    print("Invalid choice. Please enter a number between 1 and 9.")

def printAgesAverage(age_avg_dict, people):
    if checkEmpty(people):
        return
    try:
        average_age = age_avg_dict["age"] / len(people)
        print("Average age of all the people you entered: " + str(average_age))
    except Exception as e:
        print("Error calculating average age, the error is" + str(e))

def runAll(): 
    age_avg_dict = {"age": 0}
    people_dict = {}

    while True:
        try:
            #menu for user 
            for name in Func:
                print(str(name.value) + ". " + str(name.name))

            # getting from user
            menu_choice = input("Please choose from menu (1-9): ")
            
            try:
                menu_choice_enum = Func(int(menu_choice))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue
            if menu_choice_enum == Func.ADD_PERSON:
                addPerson(people_dict, age_avg_dict)
            elif menu_choice_enum == Func.FIND_BY_ID:
                findByID(people_dict)
            elif menu_choice_enum == Func.PRINT_AVERAGE_AGES:
                printAgesAverage(age_avg_dict, people_dict)
            elif menu_choice_enum == Func.PRINT_NAMES:
                printNames(people_dict)
            elif menu_choice_enum == Func.PRINT_IDS:
                printIDs(people_dict)
            elif menu_choice_enum == Func.PRINT_ALL_PERSONS:
                printAllPersons(people_dict)
            elif menu_choice_enum == Func.PERSON_BY_INDEX:
                personByIndex(people_dict)
            elif menu_choice_enum == Func.SAVE_TO_CSV:
                saveToCSV(people_dict)
                print("Data saved successfully.")
            elif menu_choice_enum == Func.EXIT:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please choose a valid option from the menu.")

            input("Press Enter to continue...")

        except Exception as e:
            print("Error executing the function, the error is: " + str(e))
            break
        
try:    
   runAll()
except KeyboardInterrupt:
    print("goodbye") 






