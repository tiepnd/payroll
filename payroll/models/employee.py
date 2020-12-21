class Employee:
    def __init__(self, name, dob, role, start_date, start_salary):
        self.name = name
        self.dob = dob
        self.role = role
        self.start_date = start_date
        self.start_salary = start_salary

    def display_employee(self):
        print("Name : ", self.name, ", BirthDay : ", self.dob, ", Role : ", self.role,
              ", StartDate : ", self.start_date,  ", StartSalary: ", self.start_salary)