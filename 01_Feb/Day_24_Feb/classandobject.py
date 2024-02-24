class Student:
    #this init function acts as constructor function
    def __init__(self, name, email, Code = None): #code is declared as none because it doesnot affect in child class
        self.name = name
        self.email = email
        self.__stCode = Code
     

    def student_Code(self):
        return {'code': self.__stCode}

    def student_details(self):
        return {'name': self.name, 'email': self.email}
    
    def set_Code(self, Code):
        print('code in setter', Code)
        if "@" in Code:
            self.__stCode = Code
            return self.__stCode
        else:
            print('must include @')

        # use getmethod for giving private variable acess to other child class
    def get_Code(self):
        return self.__stCode + " From getter setter"
    
        
    

#Inheritance
class Faculty_Enroll(Student):
    def __init__(self, name, email, faculty, Code):
        super().__init__(name, email, Code)
        self.faculty = faculty

    #polymorphism
    def student_details(self):
        details = super().student_details()
        details['faculty'] = self.faculty
        return details

    

student1 = Student('Nischal', 'nisal@gmail.com', 'we245gg')
print(student1.student_details())
# print(student1.student_Code())
print(student1.get_Code())

# it_student = Faculty_Enroll('Samir', 'samir@gmail.com', 'MIT', 'fsdfd')
# print(it_student.student_details())
# print(it_student.get_Code())