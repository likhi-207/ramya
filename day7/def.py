class Student:
    name = " "
    rollno = 0
    def __init__(self,x,y):
        self.name = x
        self.name = y
    def display_info(self):
        print("name:",self.name)
        print("rollno :",self.rollno)
student1 = Student("jam",98)
student1.name = "jam"
student1.rollno = 98
student1.display_info()
student1.__init__("bam",99)
student1.display_info()
print(student1.name)
print(student1.rollno)
