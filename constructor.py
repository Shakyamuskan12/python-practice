# class car:
#    def __init__(self,name,price): #(constructor)
#       print(self)
#       #self is the refrence to the object
# s = car("bmw",100000) #object 3 (yahan se object send karte time ek argument sath jata hai)


# class car:
#    def __init__(self,name,price):
#     self.name1=name
#     self.price2=price

# s = car("bmw",100000) #object 3
# print(s.name1)
# print(s.price2)



class car:
   def __init__(self,name,price):   #(constructor in class)
      self.name1=name
      self.price2=price 
    
   def show(self):                #(method in class)
      print(self.name1)
      print(self.price2)


s = car("bmw",100000) #object 3
s.show()

