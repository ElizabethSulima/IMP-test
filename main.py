import datetime
from application.salary import calculate_salary
from application.people import get_employees

if __name__ == '__main__':
    current_date = datetime.date.today()
    print(current_date)
    s_1 = calculate_salary()
    g_1 = get_employees()