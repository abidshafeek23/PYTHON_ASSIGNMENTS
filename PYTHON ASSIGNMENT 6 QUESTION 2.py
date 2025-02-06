class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

import employee

def main():
    emp = employee.Employee("John Doe", 50000)
    print("Employee Name:", emp.get_name())
    print("Employee Salary:", emp.get_salary())
if __name__ == "__main__":
    main()
