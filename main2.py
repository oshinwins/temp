"""class Computer:
    def config(self):
        print("i5,16gb,1tb")
com1=Computer()
Computer.config(com1)"""

"""class Computer:
    def config(self):
        print("i5,16gb,1tb")
com1=Computer()
com2=Computer()
Computer.config(com1)
Computer.config(com2)"""

"""class Computer:
    def config(self):
        print("i5,16gb,1tb")
com1=Computer()
com2=Computer()
com1.config()
com2.config()"""

#INIT FUNCTION:
#OBJECT CREATION:
"""class Computer:
    def __init__(self):
        print("in init")
    def config(self):
        print("i5,16gb,1tb")
com1=Computer()
com2=Computer()
com1.config()
com2.config()"""

class Computer:
    def __init__(self,CPU,ram):
        self.CPU=CPU
        self.ram=ram
    def config(self):
        print("conifg is",self.CPU,self.ram)
com1=Computer('i5',16)
com2=Computer('ryzen 3',8)
com1.config()
com2.config()
