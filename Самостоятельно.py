# class Human:
#     skill = 10
#     name = ''
#     surname = ''
#
#     def print_inf(self, name, surname):
#         self.name = name
#         self.surname =surname
#         print('Данные сотрудника:', self.surname, self.name)
#
#     def add_skill(self, k):
#         self.skill += k
#         print('квалификация', self.skill)
#
#
#
# p1 = Human()
# p1.print_inf('Вася', 'Рогов')
# p1.add_skill(10)

# class Human:
#     skill = 10
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         print('инициализатор')
#
#     def __del__(self):
#         print('деструктор')
#
#     def print_inf(self):
#         print('Данные сотрудника:', self.surname, self.name)
#
#     def add_skill(self, k):
#         self.skill += k
#         print('квалификация', self.skill)
#
# p1 = Human('Вася', 'Рогов')
# p1.print_inf()
# del p1
# p1.add_skill(10)

# class Point:
#     count = 0
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#     def get_coord(self):
#         return self.x, self.y
#
# p1 = Point(3, 7)
# print(p1.get_coord())
# p2 = Point(12, 0)
# print(p2.get_coord())
# p3 = Point(23, 3)
# print(p3.get_coord())
# print(Point.count)

# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print('Робот включился', self.name)
#
#     def __del__(self):
#         print('Робот отключился', self.name)
#         Robot.k -= 1
#         if Robot.k == 0:
#             print('Отключился последний робот')
#         else:
#             print('Работающих роботов осталось', Robot.k)
#
#     def sey_hi(self):
#         print('Привет, я робот', self.name)
#         Robot.k += 1
#         print('Количество работающих роботов', Robot.k)
#
# d1 = Robot('CH-1')
# d1.sey_hi()
# d2 = Robot('CH-employee.py')
# d2.sey_hi()
# d3 = Robot('CH-3')
# d3.sey_hi()
# print('\nРобот работает работу\n')
# del d1
# del d2
# del d3
# print('Количество работающих роботов', Robot.k)

# class Point:
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#
#     @staticmethod
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print('Координвты должны содержать число')
#     def get_coord(self):
#         return self.__x, self.__y
#
#
# p1 = Point(89, 10)
# # print()
# # print(p1.__dict__)
# p1.set_coord(56, 9)
# print(p1.get_coord())
#
#
# class Cat:
#     def __init__(self, name, age):
#         self.x = 'кот'
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f'Я {self.x}. Меня зовут {self.name}. Мой возраст {self.age}.'
#
#     def make_sound(self):
#         return f'{self.name} мяукает.'
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.x = 'собака'
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f'Я {self.x}. Меня зовут {self.name}. Мой возраст {self.age}.'
#
#     def make_sound(self):
#         return f'\n{self.name} гавкает.'
#
#
# c = Cat('Пушок', employee.py.5)
#
# d = Dog('Мухтар', 4)
#
# q = [c, d]
#
# for a in q:
#     print(a.info(), a.make_sound())
#
#
# class Hunman:
#     def __init__(self, surname, name, age):
#         self.surname = surname
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"\n{self.surname} {self.name} {self.age}", end=' ')
#
#
# class Student(Hunman):
#     def __init__(self, surname, name, age, group, flow, rating):
#         super().__init__(surname, name, age)
#         self.group = group
#         self.flow = flow
#         self.rating = rating
#
#     def info(self):
#         super().info()
#         print(f'{self.group}  {self.flow}  {self.rating}', end=' ')
#
#
# class Teacher(Hunman):
#     def __init__(self, surname, name, age, item, rating):
#         super().__init__(surname, name, age)
#         self.item = item
#         self.rating = rating
#
#     def info(self):
#         super().info()
#         print(f'{self.item}{self.rating}', end=' ')
#
#
# class Graduate(Student):
#     def __init__(self, surname, name, age, group, flow, rating, graduate):
#         super().__init__(surname, name, age, group, flow, rating)
#         self.graduate = graduate
#
#     def info(self):
#         super().info()
#         print(f'{self.graduate}', end='')
#
#
# groups = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
# for i in groups:
#     i.info()

class ValidString:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f"Данные {self.name} должны быть числом")
        if value <= 0:
            raise ValueError(f'Данные {self.name} должны быть положительным числом')
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class Order:
    price = ValidString()
    quantity = ValidString()

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def info(self):
        print(f'{self.name}, {self.price}, {self.quantity}')

    def total(self):
        print(self.price * self.quantity)


p = Order('apple', 5, 10)
p.info()
p.price = 100
p.info()
p.total()