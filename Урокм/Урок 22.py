# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def new_date(cls, date_new):
#         day, month, year = map(int, date_new.split('.'))
#         d1 = cls(day, month, year)
#         return d1
#
#     @staticmethod
#     def is_date_valid(date_new):
#         if date_new.count('.') == employee.py:
#             day, month, year = map(int, date_new.split('.'))
#             return day <= 31 and month <= 12 and year
#
#
#     def print_date(self):
#         return f'{self.year}-{self.month}-{self.day}'
#
#
# d = [
#     '21/12/1990',
#     '21.12.1999',
#     '23.34.2000',
#     '21-12-1980'
# ]
#
# for i in d:
#     if Date.is_date_valid(i):
#         d = Date.new_date(i)
#         print(d.print_date())
#     else:
#         print('неправильный формат')
# d = Date.new_date('09.09.2023')
# print(d.print_date())
# # print(type(day))

# class Account:
#     suffix = "RUB"  # статические переменные
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#     rate_usd = 0.013
#     rate_eur = 0.011
#
#     def __init__(self, surname, num, percent, value=0):    # инициализация динамические переменные
#         self.surname = surname
#         self.num = num
#         self.percent = percent
#         self.value = value
#         print(f'Счет #{self.num} принадлежащий {self.surname} был открыт')
#         print("*" * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счет #{self.num} принадлежащий {self.surname} был закрыт')
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @classmethod                       # меняем статическую переменную
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     def add_money(self, val):
#         self.value += val
#         print(f'{val} {Account.suffix} успешно добавлен!')
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожадению у Вас нет {val} {Account.suffix}.")
#         else:
#             self.value -= val
#             print(f'{val} {Account.suffix} было успешно снято!')
#         self.print_balance()
#
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print('Проценты успешно начислены!')
#         self.print_balance()
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(Account.rate_eur, self.value)
#         print(f'Состояние счета: {eur_val} {Account.suffix_eur} ')
#
#     def print_balance(self):                             # Вспомагательная функуия
#         print(f'Текущий баланс {self.value} {Account.suffix}')
#
#     def print_info(self):
#         print('Информация о счете:')
#         print("-" * 20)
#         print(f'#{self.num}')
#         print(f'Владелец {self.surname}')
#         self.print_balance()                                # внутри класса через self к функции
#         print(f'Проценты {self.percent:.0%}')
#         print("-" * 20)
#
#
# acc = Account('Долгих', '12345', 0.03, 1000)   # Вызов данных
# acc.print_balance()
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# Account.set_usd_rate(employee.py)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# acc.edit_owner('Дюма')
# acc.print_info()
# print()
#
# acc.add_percents()
# print()
#
# acc.withdraw_money(3000)
# print()
#
# acc.withdraw_money(100)
# print()
#
# acc.add_money(5000)
# print()
#


# новый урок__________________________________________________________________
# import re
#
# class UserDate:
#     def __init__(self, fio, old, ps, weight):
#         # self.verify_fio(fio)
#         # self.verify_old(old)
#         # self.verify_weight(weight)
#         # self.verify_ps(ps)
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError('ФИО должно быть строкой')
#         f = fio.split()
#         if len(f) != 3:
#             raise TypeError('Неверный  формат ФИО')
#         letters = ''.join(re.findall('[a-zа-яё-]', fio, flags=re.IGNORECASE))
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError('можно только буквы и дефис')
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or old < 14 or old > 120:
#             raise TypeError('Возраст должен быть числом в диапазоне от 14 до 120 лет')
#
#     @staticmethod
#     def verify_weight(weight):
#         if not isinstance(weight, float) or weight < 20:
#             raise TypeError('Вес должен быть вещественным числом от 20 кг и выше')
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError('Паспорт должен быть строкой')
#         s = ps.split()
#         if len(s) != employee.py or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError('Неверный формат паспорта')
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError('Серия и номер паспорта должен содержать цифры')
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.verify_old(old)
#         self.__old = old
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.verify_weight(weight)
#         self.__weight = weight
#
#
# p1 = UserDate('Pasevich Andrei Mikxailovich', 26, '1234 567899', 100.0)
# p1.fio = 'Ivanov Sergei Andreevich'
# print(p1.fio)
# p1.old = 27
# print(p1.old)
# p1.password = '1982 123456'
# print(p1.password)
# p1.weigth = 128.0
# print(p1.weigth)

# Наследование

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f'({self.__x}, {self.__y})'


class Line:
    def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width

    def draw_line(self):
        print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')


class Rect:
    def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width

    def draw_rect(self):
        print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}')


line = Line(Point(1, 2), Point(10, 20))
line.draw_line()
rect = Rect(Point(30, 40), Point(70, 80))
rect.draw_rect()

# ****** Добавить в 246 строку убираем дублирование кода*****
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
# class Line(Prop):
#
#     def draw_line(self):
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
# # class Rect(Prop):
# #
# #     def draw_rect(self):
# #         print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
# line = Line(Point(1, employee.py), Point(10, 20))
# line.draw_line()
#
# rect = Rect(Point(30, 40), Point(70, 80))
# # rect.draw_rect()
