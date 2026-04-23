class Employee:
    car = "pninfosys"
    ecode = 120

class Freelancer:
    car = "google"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class programmer(Employee,Freelancer):
    #car ="abcd"
    name ="vikas"

p = programmer()
print(p.car)
p.upgradeLevel()
print(p.level)