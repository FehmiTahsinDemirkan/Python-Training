class Person:
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age
        print("Person object created")
    def intro(self):
        print(self.name,self.surname,self.age)
class Student(Person):
    pass
class Teacher(Person):
    pass
p1 = Person("Fehmi","Demirkan",21)
p1.intro()

s1 = Student("Zeynep","Sıla",11)
s1.intro()

t1 = Student("dilek","ünal",54)
t1.intro()