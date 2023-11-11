import sqlite3

conn = sqlite3.connect('test.db')

print("opened Database successfully");
# conn.execute("Drop Table Grade")
# conn.execute('''CREATE TABLE Grade
#          (ID INT PRIMARY KEY     NOT NULL,
#          ClassId           INT    NOT NULL,
#          StudentId INT Not Null,
#          Grade Text Not Null);''')

def MainMenu():
    select = input('''What would you like to do?\nChange 'Grade'
'Add' Student
Add 'Class' ''')
    if select == 'Add':
        AddStudent()
    if select == "Grade":
        ChangeGrade()
    if select == "Class":
        AddClass()

def AddStudent():
    name = input("What is the students name? ")
    grade = input("What grade is the student in? ")
    # conn.execute(f"Insert into Student (Id, Name, Level) Values (1, {name}, {grade})")
    cursor = conn.execute("SELECT * from Student")
    count = 0
    for row in cursor: 
        print(row[0])
        count += 1
    
        
    conn.execute(f"INSERT INTO Student (ID,NAME,Level) \
      VALUES ({count}, '{name}', {grade})");
    
    conn.commit()

def AddClass():
    name = input("What is the class name? ")
    # conn.execute(f"Insert into Student (Id, Name, Level) Values (1, {name}, {grade})")
    cursor = conn.execute("SELECT * from Class")
    count = 0
    for row in cursor: 
        print(row[0])
        count += 1
    
        
    conn.execute(f"INSERT INTO Class (ID,NAME) \
      VALUES ({count}, '{name}')");
    conn.commit()

def ChangeGrade():
    studentName = input("What is the name of the student you want to grade? ")
    cursor = conn.execute(f"SELECT Id from Student Where Name = '{studentName}'")
    for row in cursor:
        studentId = row[0]
    # print(hasattr(studentId, 'value'))
    className = input("What class? ")
    course = conn.execute(f"SELECT Id from Class Where Name = '{className}'")
    for row in course:
        classId = row[0]
    grade = input("What Grade? ")
    conn.execute(f"Update Grade set Grade = '{grade}' where ClassId = {classId} AND StudentId = {studentId}")
    conn.commit()
    if conn.total_changes == 0:
        all = conn.execute("SELECT * from Grade")
        count = 0
        for row in all: 
            print(row[0])
            count += 1
        conn.execute(f'''Insert Into Grade (Id, ClassId, StudentId, Grade)\
                     Values ({count}, {classId}, {studentId}, '{grade}')''');
        conn.commit()
    studentWithGrade = conn.execute(f'''Select s.Name, g.Grade from Student s join Grade g on g.StudentId = s.Id where s.Id = {studentId}''');
    for row in studentWithGrade:
        print(row)
        
  

    
  
        
    
MainMenu()