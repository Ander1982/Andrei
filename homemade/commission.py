from homemade.salary import SalaryEmployee


class CommissionEmployee(SalaryEmployee):
    """ Торговые представители, фиксированная зарплата + комиссия"""

    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate(self):
        fixed = super().calculate()
        return fixed + self.commission
