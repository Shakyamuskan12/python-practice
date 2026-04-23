class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def result(self):
        if self.marks >= 40:
            print(self.name,"pass")
        else:
            print(self.name,"fail" )

s1 = student("john",90)
s2 = student("ram",30)
s1.result()
s2.result() 