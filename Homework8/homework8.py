class Student:

    def __init__(self,name,surname,age,avg_grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.avg_grade = avg_grade

    def change_grade(self,new_grade):
        self.avg_grade = new_grade




student1 = Student("Alex","Efremov",24,90)


print(f"Name: {student1.name}\nSurname: {student1.surname}\nAge: {student1.age}\nAverage grade: {student1.avg_grade}\n")


student1.change_grade(95)


print(f"Name: {student1.name}\nSurname: {student1.surname}\nAge: {student1.age}\nNew AVG grade: {student1.avg_grade}")


