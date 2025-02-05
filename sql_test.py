import sqlalchemy
USERNAM = "myuser"
PASSWORD = "mypassword" 
DB_HOSTNAME = "localhost"
DB_NAME = "college"

#provid DataBase to python and create connection to DataBase
DATABASE_URI = "postgresql://" + USERNAM + ":" + PASSWORD + "@" + DB_HOSTNAME + "/" + DB_NAME   
engine = sqlalchemy.create_engine(DATABASE_URI)  
#Create a new SQL queries
my_query_avg = """  
SELECT AVG(age) as ages_avg FROM students
"""
my_query_count =  """  
SELECT COUNT(*) FROM students
"""
my_query_add_student =  """  
INSERT INTO students (id, name, age, email)
VALUES(:id, :name, :age, :email);
"""

with engine.connect() as connection:
    result_count = connection.execute(sqlalchemy.text(my_query_count))
    count = result_count.scalar() 
    print("number of students: " + str(count))

    result_avg = connection.execute(sqlalchemy.text(my_query_avg))
    avg_age = result_avg.scalar()  
    print("Average age of students: " + str(avg_age))

    new_student_data = {
        "id": 323074005,  
        "name": "Idan Michael", 
        "age": 23,  
        "email": "idan.mic6@gmail.com"  
    }

    connection.execute(sqlalchemy.text(my_query_add_student), new_student_data)
    print("The new student is: " + new_student_data["name"])
   