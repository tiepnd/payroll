import csv
from models.employee import Employee
from common.service import string_to_date, get_age, get_total_year, get_current_salary

with open('data/employee.csv', encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count != 0:
            employee = Employee(row[0], string_to_date(row[1]), row[2], string_to_date(row[3]), float(row[4]))
            employee.display_employee()
            print(
                "Age:", get_age(employee.dob), ", Total year:", get_total_year(employee.start_date),
                "Current Salary:", get_current_salary(employee.start_date, employee.start_salary)
            )
        line_count += 1
