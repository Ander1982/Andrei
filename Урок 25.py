# множественное наследование

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + ' is sleeping')
#
#
# class Pet(Creature):
#     def __init__(self, age):
#         self.age = age
#         print('Игтцталтзатор класс Pet')
#     def play(self):
#         print(self.name + ' is playing')
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + ' is barking')
#
#
# dog = Dog('Buddy')
# dog.bark()
# dog.play()
# dog.sleep()

# class A:
#     def __init__(self):
#         print('Иницилизатор A')
#
#
# class AA:
#     def __init__(self):
#         print('Иницилизатор AA')
#
#
# class B(A):
#     def __init__(self):
#         print('Ишициализ B')
#
#
# class C(AA):
#     def __init__(self):
#         print(' С')
#
#
# class D(B, C):
#     def __init__(self):
#         B.__init__(self)
#         C.__init__(self)
#         print('D')
#
#
# d = D()
# print(D.mro())
# print(D.__mro__)

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'({self.y}, {self.x})'
#
#
# class Styles:
#     def __init__(self, color="red", width=1):
#         print('Инициизация Styles')
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, color, width):
#         print('Инициалтз Pos')
#         self._sp = sp
#         self._ep = ep
#         super().__init__(color, width)
#
#
# class Line(Pos, Styles):
#     def draw(self):
#         print(f' Оисоыр {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# l1 = Line(Point(10, 10), Point(100, 100), 'green', 5)
# l1.draw()
#
# Миксины (примеси)

# class Displayer:
#     @staticmethod
#     def display(massage):
#         print(massage)
#
# class LoggerMixin:
#     def log(self, message, filename='logfile.txt'):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#
#     def display(self, messege):
#         Displayer.display(messege)
#         self.log(messege)
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=""):
#         super().log(message, filename='subclasslog.txt')
#
#
# subclass = MySubClass()
# subclass.display('Строка будет печататься и сохраняться в файле')

# class Goods:
#     def __init__(self, name, weight, price):
#         print('Init Goods')
#         super().__init__()
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f'{self.name}, {self.weight}, {self.price}')
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print('Init MixinLog')
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def save_sell_log(self):
#         print(f"{self.id}: товар продан в 00:00 часов")
#
#
# class NoteBook(Goods, MixinLog):
#     pass
#
#
# n = NoteBook('HP', 1.5, 35000)
# n.print_info()
# n.save_sell_log()

# Перегрузка операторов

class Clock:
    __DAY = 86400

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError('Секунды дложнв быть челыми')
        self.sec = sec % self.__DAY

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый оперент тип данных Clock')
        return self.sec == other.sec

    def __eq__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый оперент тип данных Clock')
        return Clock(self.sec + other.sec)

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else "0" + str(x)


c1 = Clock(600)
c2 = Clock(200)
if c1 == c2:
    print('Впемя одтинаковое')
else:
    print('Время разное')
c3 = c1 + c2
print('c1:', c1.get_format_time())
print((c2.get_format_time()))
# print((c3.get_format_time()))
