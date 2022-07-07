

import datetime
from multiprocessing import managers



class Employee:
    
    def __init__(self, name, age, salary, employment_year):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_year = employment_year
        
    def get_working_year(self):

        return int(datetime.date.today().year) - self.employment_year
        
    
   #Employee class here
   

class Manager():
    
    def __init__(self, name, age, salary, employment_year,bonus_percentage):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_year = employment_year
        self.bonus_percentage =bonus_percentage
    def get_working_year(self):

        return int(datetime.date.today().year) - self.employment_year
    def get_bonus(self):
        return self.bonus_percentage * self.salary
    #Manager class here
    pass

def showList(List, mySelection):
     for emp in List:
         if mySelection == 1:
             print("Name : " + str(emp.name))
             print("Age : " + str(emp.age))
             print("Salary : " + str(emp.salary))
             print("Working years : "+str(emp.get_working_year()))
             print("--------------------")
         if mySelection == 2:
             print("Name : " + str(emp.name))
             print("Age : " + str(emp.age))
             print("Salary : " + str(emp.salary))
             print("Working years : "+str(emp.get_working_year()))
             print("Bonus : " + str(emp.get_bonus()))
             print("--------------------")
             

        
def addToList(mySelection):
    if mySelection == 3:
        myEmp = Employee(input("Employee name: "),
                         input("Employee age: "),
                         int(input("Employee Salary: ")),
                         int(input("Employee starting year: ")))
        return myEmp
    if mySelection == 4:
        myManager = Manager(input("Manager name: "),
                            input("Manager age: "),
                            int(input("Manager salare: ")),
                            int(input("Manager starting year: ")),
                           float(input("Manager bonus percentage: ")))

        return myManager

def showOptions():
    
    print("Options:")

    print("	1. Show Employees")
    print("	2. Show Managers")
    print("	3. Add An Employee")
    print("	4. Add A Manager")
    print("	5. Exit\n")
    selection = input("Select an option: ")
    return selection
    
def main():
	# main code here
 
 employersList = [Employee("Ahmed",44,1222,2020),
                  Employee("Ali",34,1222,2020),
                  Employee("Nasser",33,1000,1992)]
 
 manegersList = [Manager("Aziz",44,4000,1967,.5),
                  Manager("Abdullah",22,2000,1992,0.5),
                  Manager("Fhad",33,5000,1940,0.5)]
 print("Welcome to HR Pro 2019")
 userSelection =0
 while userSelection != 5:
     if userSelection >5 and userSelection <1:
         print(" your option is invalid\n")
     else:
         userSelection = int(showOptions())
         if userSelection == 1 :
             showList(employersList, userSelection)
         if userSelection == 2 :
             showList(manegersList, userSelection)
         if userSelection == 3 :
             employersList.append(addToList(3))
         if userSelection == 4:
             manegersList.append(addToList(4))

if __name__ == '__main__':
	main()
