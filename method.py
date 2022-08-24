class Student:
    school='gpg'---#class variable
    def __init__(self,m1,m2,m3):
        self.m1=m1---#instance variable
        self.m2=m2   #instance variable
        self.m3=m3   #instance variable
    def avg(self):
        return (self.m1+self.m2+self.m3)/3


s1=Student(34,47,32)  #s1 and s2 are objects where we are passing the values
s2=Student(89,32,12)
print(s1.avg())
print(s2.avg())