"""class Student:
    school='gpg'  #class variable
    def __init__(self,m1,m2,m3):
        self.m1=m1  #instance variable
        self.m2=m2   #instance variable
        self.m3=m3   #instance variable
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    def get_m1(self):  #accessor method
        return self.m1
    def set_m1(self,value):   #mutator method
        self.m1=value


s1=Student(34,47,32)  #s1 and s2 are objects where we are passing the values
s2=Student(89,32,12)

print(s1.m1)"""

#Class method
"""class Student:
    school='gpg'  #class variable
    def __init__(self,m1,m2,m3):
        self.m1=m1  #instance variable
        self.m2=m2   #instance variable
        self.m3=m3   #instance variable
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    @classmethod
    def info(cls):
        return cls.school

s1=Student(34,47,32)  #s1 and s2 are objects where we are passing the values
s2=Student(89,32,12)

print(s1.m1)
print(Student.info())"""

#STATIC METHOD:

class Student:
    school='gpg'  #class variable
    def __init__(self,m1,m2,m3):
        self.m1=m1  #instance variable
        self.m2=m2   #instance variable
        self.m3=m3   #instance variable

    def avg(self):
            return (self.m1 + self.m2 + self.m3) / 3
    @classmethod
    def getschool(cls):
            return cls.school

    @staticmethod
    def info():
            print("this is student class....in the module")


s1 = Student(34, 47, 32)  # s1 and s2 are objects where we are passing the values
s2 = Student(89, 32, 12)


print(Student.getschool())
Student.info()


