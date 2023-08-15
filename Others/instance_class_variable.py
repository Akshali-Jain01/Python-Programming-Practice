class Employee:
    salary = 10000
    Increase = 1.5
    def __init__(self,name,salary,address):
        self.name = name
        self.salary = salary
        self.address = address
        self.Increase =2.0
    def display(self):
        print(self.name,self.salary,self.address,self.Increase,Employee.Increase)
    # @ is used to define the decorator to change the variable in class
    @classmethod
    