class calculator:
    def __init__(self,a,b):   #constructor
        self.a=a
        self.b=b 
        
    def add(self):           #Method
        print(self.a + self.b)

    def sub(self):
        print(self.a - self.b)

    def mul(self):
        print(self.a * self.b)

    def div(self):
        print(self.a / self.b)


s = calculator(5,10)    #object 3
s.add()
s.sub()
s.mul()     
s.div() 