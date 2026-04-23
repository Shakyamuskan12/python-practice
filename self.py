# self refers to the insatance of the class
# it is automatically passed with a function call
# from an object.
class Empolyee:
    company = "pninfosys"
    def getSalary(self,a): #automatic pass parameter
        print("Salary is 100k")
        print(f"Salary is {self.salary}")
        print(f"Salary is {self.salary}")
        print(f"Salary is this empolyee working in {self.company} is {self.salary}")

rohit = Empolyee()
rohit.salary = 10000
rohit.getSalary(3000) #Employee.getsalary(rohit)