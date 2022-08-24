#INNER CLASS(CLASS INSIDE A CLASS):

class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
    class laptop:
        def __init__(self):
            self.brand='hp'
            self.cpu='i3'
            self.ram=8

        def show(self):
                print(self.brand, self.cpu,self.ram)
s1=Student('oshin',2)
s2=Student('oshin2',4)
s1.show()
lap1=Student.laptop()