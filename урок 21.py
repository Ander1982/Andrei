#
# class Person:
#     skill = 10
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         print('Инициалатор')
#
#
#     def print_info(self):
#         print('Данные сотрудников:', self.name, self.surname)
#
#
#     def add_skill(self, k):
#         self.skill = self.skill + k
#         print('Квалификация сотрудника', self.skill)
#
# p1 = Person('Виктор', 'Резник')
# p1.print_info()
# # p1.add_skill(9)
# p2 = Person('Анна', 'Долгих')
# p2.print_info()
# p2.add_skill(2)

# class Point:
#     count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#     def get_coord(self):
#         return self.x, self.y
#
# p1 = Point(5, 10)
# print(p1.get_coord())
# p2 = Point(2, 7)
# print(p2.get_coord())
# p3 = Point(10, 20)
# print(p3.get_coord())


# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print('Инициализация робота:', self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, 'выключается')
#         Robot.k -= 1
#         if Robot.k == 0:
#             print(self.name, 'был последний')
#         else:
#             print('Работающих роботов осталось', Robot.k )
#
#     def say_hi(self):
#         print('Привет! меня зовут:', self.name)
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# print('Численность роботов:', Robot.k)
#
#
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# print('Численность роботов:', Robot.k)
#
# droid3 = Robot('К5-100')
# droid3.say_hi()
# print('Численность роботов:', Robot.k)
#
# print('\nЗдесь работают работу\n')
#
# print('Роботы закончили работу')
# del droid1
# del droid2
# del droid3
# print('Численность роботов:', Robot.k)


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
        # if isinstance(x, int) or isinstance(x, float) and isinstance(y, int) or isinstance(y, float):
        if Point.__check_value(x) and Point.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            print('Кординаты должны быть числами')


    def get_coord(self):
        return self.__x, self.__y

p1 = Point('aaa', 10)
# print(p1.__x, p1.y)
# p1.__x = 100
# p1.__y = 'abc'
# print(p1.__x, p1.__y)
# p1.set_coord(20.8, 50)
print(p1.get_coord())
print(p1.__dict__)
# print(Point.__dict__)
