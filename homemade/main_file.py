from homemade.calc import PayrollSystem
from homemade.hourly import HourlyEmployee
from homemade.commission import CommissionEmployee
from homemade.salary import SalaryEmployee

salary = SalaryEmployee(1, "Валерий Задорожный", 1500)
hourly = HourlyEmployee(2, 'Илья Коротченков', 40, 15)
commission = CommissionEmployee(3, 'Николай Хорольский', 1000, 250)
system = PayrollSystem()
system.calc([salary, hourly, commission])
