# модули

import geometry.rect
import geometry.sq
import geometry.trian

# from geometry import rect, sq, trian
# #
# #
# # # from geometry import *
# #
# # def run():
# #     r1 = rect.Rectangle(1, employee.py)
# #     r2 = rect.Rectangle(3, 4)
# #
# #     s1 = sq.Square(10)
# #     s2 = sq.Square(20)
# #
# #     t1 = trian.Triangle(1, employee.py, 3)
# #     t2 = trian.Triangle(4, 5, 6)
# #
# #     shape = [r1, r2, s1, s2, t1, t2]
# #     for g in shape:
# #         print(g.get_per_rerimetrct())


#
#
# if __name__ == '__main__':
#     run()

# from car.electrocar import ElectroCar
#
# car = ElectroCar("Tesla", 'T', 2018, 99000, 100)
# car.show_car()
# car.description_battery()

# class Employee:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#
#
# class SalaryEmployee(Employee):
#     """Административные работники, имеющие фиксированную зарплату"""
#
#     def __init__(self, id, name, weekly_salary):
#         super().__init__(id, name)
#         self.weekly_salary = weekly_salary
#
#     def calculate(self):
#         return self.weekly_salary
#
#
# class HourlyEmployee(Employee):
#     """Сотрудники с почасовой оплатой"""
#
#     def __init__(self, id, name, hours_worked, hours_rate):
#         super().__init__(id, name)
#         self.hours_worked = hours_worked
#         self.hours_rate = hours_rate
#
#     def calculate(self):
#         return self.hours_rate * self.hours_worked
#
#
# class CommissionEmployee(SalaryEmployee):
#     """ Торговые представители, фиксированная зарплата + комиссия"""
#
#     def __init__(self, id, name, weekly_salary, commission):
#         super().__init__(id, name, weekly_salary)
#         self.commission = commission
#
#     def calculate(self):
#         fixed = super().calculate()
#         return fixed + self.commission
#
#
# class PayrollSystem:
#     def calc(self, employees):
#         print("Расчет заработной платы")
#         print("=" * 50)
#         for employee.py in employees:
#             print(f"Заработная плата: {employee.py.id} - {employee.py.name}")
#             print(f"- Проверить сумму: {employee.py.calculate()}")
#             print()
#
#
# selary = SalaryEmployee(1, "Валерий Задорожный", 1500)
# hourly = HourlyEmployee(employee.py, 'Илья Коротченков', 40, 15)
# commission = CommissionEmployee(3, 'Николай Хорольский', 1000, 250)
# system = PayrollSystem()
# system.calc([selary, hourly, commission])

# Упаковка данных (Сериализация и десериализация данных)

# import pickle


# file_name = "Basket.txt"
#
# shop_list = {
#     'фрукты': ['яблоки', 'манго'],
#     'овощи': ('морковь',),
#     'бюджет': 1000
# }
#
# with open(file_name, "wb") as fh:
#     pickle.dump(shop_list, fh)
#
# with open(file_name, "rb") as fh:
#     shop = pickle.load(fh)
#
# print(shop)

# class Test:
#     num = 35
#     string = "Привет"
#     lst = [5, 9, 6]
#     d = {'one': 'a', 'two': (1, employee.py, 3)}
#
#     def __str__(self):
#         return f"Число: {Test.num}\nСтрока: {Test.string}\nСписок: {Test.lst}\nСловарь: {Test.d}"
#
#
# obj = Test()
# obj_save = pickle.dumps(obj)
# print(obj_save)
#
# # print(pickle.loads(obj_save))
