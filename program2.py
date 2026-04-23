class Test:
    def __init__(self, x):
        self.x = x
    
t = Test(5)
print(t)
# ye useless memory address dikhta hai
# <__main__. Test


# example with __str__()
class Test:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return f"value is {self.x}"
    

t = Test(5)
print(t)
# ab readable output mila
# __str__() = object ko human readable format me print karne ke lite
#__init_ python ka constructor 