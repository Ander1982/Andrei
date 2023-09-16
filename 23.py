# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangele(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError
#
#     def area(self):
#         return self.__width * self.__height
#
#
# rect = Rectangele(10, 20, 'green')
# print(rect.color)
# print(rect.area())

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x}, {self.__y})'
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
# #
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print('оооллл')
# #
# class Line(Prop):
#     def draw_line(self):
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print('оооллл')
#
# class Rect(Prop):
#
#     def draw_rect(self):
#         print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coord(Point(20, 40), Point(100, 200))
# line.draw_line()
# rect = Rect(Point(1, 2), Point(10, 20))
# rect.set_coord(Point(10.5, 56), Point(48, 95))
# rect.draw_rect()

# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f'Прямокгольник:\nЩирина{self.width}\nВысота:{self.height}')
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         super().__init__(width, height)
#         self.fon = background
#
#     def show_rect(self):
#         print('Fon', self.fon)
#         super().show_rect()
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, border):
#         super().__init__(width, height)
#         self.border = border
#         print('Pamka:', self.border)
#
#
# sh = RectFon(400, 200, 'yellow')
# sh.show_rect()
# print()
# sh2 = RectBorder(600, 300, '1px solid red')
# sh2.show_rect()

# class Vector(list):
#     def __str__(self):
#         return ' '.join(map(str, self))
#
# v = Vector([1, 2, 3])
# print(v)

# Перезгкзеа меьотор

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x}, {self.__y})'
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print('оооллл')
#
#  class Line(Prop):
#     def draw_line(self):
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print('оооллл')
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coord(Point(20, 40), Point(100, 200))
# line.draw_line()

# Aбстрактные методы

from math import pi


class Table:
    def __init__(self, width=None, length=None, radius=None):
        if radius is None:
            self._width = width
            self._length = length
        else:
            self._radius = radius

    def calc_area(self):
        raise NotImplementedError('В дочернем клвссе должкн быть определен медод calc_areal')


class SqTable(Table):
    def calc_area(self):
        return self._width * self._length


class RoundTable(Table):
    def calc_area(self):
        return round(pi * self._radius ** 2)


t = SqTable(10, 20)
print(t.__dict__)
print(t.calc_area())

t1 = RoundTable(radius=20)
print(t1.__dict__)
print(t1.calc_area())
