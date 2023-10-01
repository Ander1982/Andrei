from homemade.employee import Employee


class HourlyEmployee(Employee):
    """Сотрудники с почасовой оплатой"""

    def __init__(self, id, name, hours_worked, hours_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hours_rate = hours_rate

    def calculate(self):
        return self.hours_rate * self.hours_worked
