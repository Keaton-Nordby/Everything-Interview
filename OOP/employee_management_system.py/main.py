# Custom Exception 

# Model Classes
class Department:
    def __init__(self, dept_id, name):
        print("Department class called")
        self.dept_id = dept_id
        self.name = name

class Employee:
    def __init__(self, name, department):
        print("Employee class called")
        self.name = name
        self.department = department
        
    def __str__(self):
        return f"{self.name} ({self.department.name})"

class Project:
    def __init__(self, name):
        print("Project class called")
        self.name = name
        self.employee_hours = {}
        
    def add_work(self, employee, hours):
        if employee in self.employee_hours:
            self.employee_hours[employee] += hours
        else:
            self.employee_hours[employee] = hours
            
    def total_hours(self):
        return sum(self.employee_hours.values())


# In Memory Storage
departments: dict[int, Department] = {}
employees: dict[str, Employee] = {}
projects: dict[str, Project] = {}

PROJECT_BUDGET = 150


# Functionality
def add_department():
    print("add_department called")
    name = input("Enter department name: ")
    dept_id = max(departments.keys(), default=0) + 1
    departments[dept_id] = Department(dept_id, name)
    print("Department added!!@")
    

def view_departments():
    pass

def add_emplopyee():
    pass

def list_employees():
    pass

def add_work():
    pass

# Summary Generation (With Exception)
def show_summary():
    pass


# Initialization
