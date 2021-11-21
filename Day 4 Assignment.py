class Student:
    def getStudentDetails(self):
        self.rollno=input("Enter Roll Number : ")
        self.name = input("Enter Name : ")
        print(self.rollno,self.name)
        
class Teacher:
     def getTeacherDetails(self):
          self.name = ('Vipin Kumar')
          self.eSalary = ('30000') 
          print(self.eSalary,self.name)
           
s1=Student()
s1.getStudentDetails()
print(s1)

s2=Teacher()
s2.getTeacherDetails()
print(s2)