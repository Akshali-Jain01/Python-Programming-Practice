class first:
    def __init__ (self):
        self.a=int(input("enter a"))
        self.b=int(input("enter b"))


      

class second(first):
    def __init__ (self):
        # print("bye")
        super().__init__()
        # print("hello")
        print(self.a+self.b)
        print()


# d1=first()
# d1.show()
d2=second(10)
# d2.show()