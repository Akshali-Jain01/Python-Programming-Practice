class Aj:
    pass
std1 =Aj()
std2=Aj()
std1.name="Akshali"
std1.s_class="11"
std1.address="udr"
print(std1)
print(std1.name)
std2.name="Akshali"
std2.course="11"
std2.hod="udr"
print(std2.__dict__)
print(std2.name)
###############################################
class computer:
    def display(self):
        print("i am working with computer properly")
    def vijay(self):
        print("i am vijay")
d1=computer()
print(type(d1))
d1.vijay()
d1.display()
#######################################################
class demo:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary = salary
    def putdata(self):
        print(self.name,self.age,self.salary)
d1=demo("ramesh",35,30000)
d1.putdata()
