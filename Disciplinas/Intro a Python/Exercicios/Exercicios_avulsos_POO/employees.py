class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department 
             
    def employee_data_bank(self, dic):
        self.employee_dict = dic
        return self.employee_dict

    def calculate_emp_salary(self, salary, hours_worked):
        emp_name = str(input())
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = (overtime * (salary / 50))
            self.employee_dict[emp_name][1] += overtime_amount
    
    def emp_assign_department(self, emp_name):
        new_department = str(input())
        self.employee_dict[emp_name][2] = new_department

    def print_employee_details(self):
        employee = str(input())
        print(dic[employee])

dic = {"ADAMS": ["E7876", 50000, "ACCOUNTING"], "JONES": ["E7499", 45000, "RESEARCH"], "MARTIN": ["E7900", 50000, "SALES"], "SMITH": ["E7698", 55000, "OPERATIONS"]}

s = 