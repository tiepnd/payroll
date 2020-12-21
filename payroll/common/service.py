from datetime import datetime
import math

salary_increase = 0.06
salary_increase_dependent = 12


def string_to_date(string_date):
    date = datetime.strptime(string_date, '%Y%m%d')
    return date


def get_age(dob):
    today = datetime.today()
    time_difference = today - dob
    days = time_difference.days
    return math.floor(days / 365)


def get_total_year(start_date):
    today = datetime.today()
    time_difference = today - start_date
    months = math.floor(time_difference.days / 30)
    years = math.floor(months / 12)
    if years > 0:
        return str(years) + " năm, " + str(months - years * 12) + " tháng,"
    else:
        return str(months) + " tháng,"


def get_current_salary(start_date, salary):
    today = datetime.today()
    time_difference = today - start_date
    months = math.floor(time_difference.days / 30)
    if months > salary_increase_dependent:
        return salary + salary * salary_increase
    else:
        return salary
