"""class Computer:
    pass
c1=Computer()
print(id(c1))"""

"""class Computer:
    pass
c1=Computer()
c2=Computer()
print(id(c1))
print(id(c2))"""

"""class Computer:
    def __init__(self):
        self.name="oshin"
        self.age=22
c1=Computer()
c2=Computer()
print(c1.name)
print(c2.name)"""

"""class Computer:
    def __init__(self):
        self.name="oshin"
        self.age=22
    def update(self):
        self.age=30
c1=Computer()
c2=Computer()
c1.name="oshin2"
c1.age=23
c1.update()
print(c1.name)
print(c2.name)"""


"""class Computer:
    def __init__(self):
        self.name="oshin"
        self.age=22
    def update(self):
        self.age=30
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False
c1=Computer()
c2=Computer()
if c1.compare(c2):
    print("they are same")
print(c1.name)
print(c2.name)"""

class Computer:
    def __init__(self):
        self.name="oshin"
        self.age=22
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False


c1 = Computer()
c1.age=30
c2 = Computer()

if c1.compare(c2):
    print("they are same")
else:
    print("they are different")
print(c1.name)
print(c2.name)


