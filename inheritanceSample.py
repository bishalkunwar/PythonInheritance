#Python program to perform the sample of multi level inheritance.


global studentCount = 0
global teacherCount = 0
global again = 'y' or 'Y'
student_records = [] #pseudo: if student from option should append on this container else on the teacher container
teacher_records = []
class student:  #defining the student class
    def __init__(self, name, idNum, semseter):  #variables of student class
        self.name = name
        self.idNum = idNum
        self.semester = semseter

class teacher:   #definiing the class teacher
    def __init__(self,teacherID,faculty):  #variables of teachere class
        self.teacId = teacherID
        self.faculty = faculty


class sunway(student,teacher): #class sunway that inherits multilevel class
    def __init__(self,choice):
        self.option = choice
        super.__init__() #This means calling constructor of parent class like, name from the student class. where first sunway will get runa dn later on will call the constructor of parent class student.
       # but i am little bit confused about MRO and calling both constructors at the same time but yes, the constructor starts getting called from left to right.

    def takingInput(self):
        while again:
        option = int(input("Enter the choice:-\n\n1: Student\n2: Teacher"))
        self.name = input("Enter the name: ")
        if option == 1:
            self.idNum = input("Enter the student id number: ")
            self.semester = input("Enter the current semester: ")
        elif option == 2:
            self.teacId= input("Enter the Teacher id number: ")
            self.faculty = input("Enter the Faculty group: ")

        else:
            print("Sorry,wrong value\n\nProgram terminated.")
            breakpoint()
            
    def display(self):
        print("Name: ",self.name)
        #how to make that option variable working for display method also.
        #pseudocode below:
        if option == 1:
            print("student id: ",self.idNum)
            print("Semester: ",self.semester)
        else:
            print("Teacher id: ",self.teacId)
            print("Faculty: ",self.faculty)


#seeking to make the loop run on display time also and list implementation.