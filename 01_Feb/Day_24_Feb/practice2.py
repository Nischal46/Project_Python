#Write a program by creating an 'Employee' class having the following functions and print the final salary.
#1 - 'getInfo()' which takes the salary, number of hours of work per day of employee as parameters
#2 - 'AddSal()' which adds $10 to the salary of the employee if it is less than $500.
#3 - 'AddWork()' which adds $5 to the salary of the employee if the number of hours of work per day is more than 6 hours.

class Employeee:

    def __init__(self, name, salary, work_hour):
        self.name = name
        self.salary = salary
        self.work_hour = work_hour

    def get_info(self):
        details = dict()
        details['name'] = self.name
        details['salary'] = '$' + str(self.salary)
        details['work_hour'] = self.work_hour
        return details
    
    def add_salary(self):
        if(self.salary < 500):
            bonus = self.salary + 10
            return bonus
        
        else: 
            return self.salary
        
        
    def add_Work(self):
        bonus = self.salary + 5 if self.work_hour > 6 else self.salary

        return bonus


emp1 = Employeee('Nischal', 400, 7)
print(emp1.get_info())
print(emp1.add_salary())
print(emp1.add_Work())