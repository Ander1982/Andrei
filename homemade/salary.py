from homemade.employee import Employee


class SalaryEmployee(Employee):
    """Административные работники, имеющие фиксированную зарплату"""

    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate(self):
        return self.weekly_salary


# salary = DZ_28.salary.SalaryEmployee(1, "Валерий Задорожный", 1500)
