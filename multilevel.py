class person:
    conuntry = "India"

    def takeBreath(self):
        print("gwalior")

class Employee(person):
    company = "Honda"

    def getSalary(self):
        print("salary 10000")
    def takeBreath(self):
        super().takeBreath()
        print("pninfosys")

class programmer(Employee):
    company = "Fiverr"

    def getSalary(self):

        print(f"No salary to programmers")

    def takeBreath(self):
        super().takeBreath()
        print("I am an programmer so I am Luckily breathing++.. ")

p = programmer()
p.takeBreath()