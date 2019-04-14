class Employee:
    def __init__(self, name, last_name, rate_per_hour=100,):
        self.name = name
        self.last_name = last_name
        self.rate_per_hour = rate_per_hour
        self.worked_hours = 0

    def register_time(self, hours):
        self.worked_hours = hours

    def pay_salary(self):
        if self.worked_hours > 8:
            to_pay = 8* self.worked_hours + (self.worked_hours - 8) * self.rate_per_hour
        else:
            to_pay = self.worked_hours * self.rate_per_hour
        return to_pay


def test_employee_initialization():
    employee = Employee('Jan', 'Nowak', 100.0)
    assert employee.name == 'Jan'
    assert employee.last_name == "Nowak"
    assert employee.rate_per_hour == 100.0


def test_employee_register_time():
    employee = Employee('Jan', 'Nowak', 100.0)
    assert employee.worked_hours == 0
    employee.register_time(5)
    assert employee.worked_hours == 5


def test_employee_pay_salary():
    employee = Employee('Jan', 'Nowak', 100.0)
    assert employee.pay_salary() == 0
    employee.register_time(6)
    assert employee.pay_salary() == 6 * 100
    employee.register_time(10)
    assert employee.pay_salary()
