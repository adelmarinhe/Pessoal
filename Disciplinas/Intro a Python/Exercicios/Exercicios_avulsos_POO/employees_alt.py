class Employee:
    def __init__(self, employee_base: dict):
        self.employee_base = employee_base

    def calculate_emp_salary(self, salary, hours_worked):
        overtime_amount = 0
        emp_name = str(input())
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = (overtime * (salary / 50))
            self.employee_base[emp_name][1] += overtime_amount
    
    def emp_assign_department(self, emp_name):
        new_department = str(input())
        self.employee_base[emp_name][2] = new_department

    def print_employee_details(self):
        employee = str(input())
        print(self.employee_base[employee])

    def show_employees(self):
        return self.employee_base

data_base = {"ADAMS": ["E7876", 50000, "ACCOUNTING"], "JONES": ["E7499", 45000, "RESEARCH"], "MARTIN": ["E7900", 50000, "SALES"], "SMITH": ["E7698", 55000, "OPERATIONS"]}

e = Employee(data_base)