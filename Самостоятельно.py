
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
# d2 = Robot('CH-2')
# d2.sey_hi()
# d3 = Robot('CH-3')
# d3.sey_hi()
# print('\nРобот работает работу\n')
# del d1
# del d2
# del d3
# print('Количество работающих роботов', Robot.k)

class Point:

    def __init__(self, x, y):
        self.__x = self.__y = 0
        if Point.__check_value(x) and Point.__check_value(y):
            self.__x = x
            self.__y = y


    @staticmethod
    def __check_value(z):
        if isinstance(z, int) or isinstance(z, float):
            return True
        return False

    def set_coord(self, x, y):
        if Point.__check_value(x) and Point.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            print('Координвты должны содержать число')
    def get_coord(self):
        return self.__x, self.__y


p1 = Point(89, 10)
# print()
# print(p1.__dict__)
p1.set_coord(56, 9)
print(p1.get_coord())



