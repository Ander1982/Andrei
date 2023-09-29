from abc import ABC, abstractmethod


# class Chess(ABC):
#     def draw(self):
#         print('нарисовать шахматную фигуру')
#
#     @abstractmethod
#     def move(self):
#         pass
#
#
# class Queen(Chess):
#     def move(self):
#         print('Ферзь перемещен на e2e4')
#
#
# q = Queen()
# q.move()
# q.draw()


# class Currency(ABC):
#     rub = 'RUB'
#
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     @abstractmethod
#     def print_value(self):
#         print(self.value, end=" ")
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = 'USD'
#
#     def convert_to_rub(self):
#         return round(self.value * Dollar.rate_to_rub, 2)
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, '=', self.convert_to_rub(), Currency.rub)
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = 'EUR'
#
#     def convert_to_rub(self):
#         return round(self.value * Euro.rate_to_rub, 2)
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, '=', self.convert_to_rub(), Currency.rub)
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
#
# print('*' * 50)
# for elem in d:
#     elem.print_value()
#
# print('*' * 50)
# for elem in e:
#     elem.print_value()

#  интерфейс

# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print('Child display1')
#
#
# class GrandChild(Child):
#     def display2(self):
#         print('GrandChild display2')
#
#
# gc = GrandChild()
# gc.display2()
# gc.display1()

# Вложенные классы

# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def outer_method():
#         print('Статический метод')
#
#     def obj_method(self):
#         print('метод экземпляра')
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.obj = obj
#             self.inner_name = inner_name
#
#         def inner_method(self):
#             print('Вложенный класс')
#             print(MyOuter.age)
#             MyOuter.outer_method()
#             print(self.obj.name)
#
# out = MyOuter('внешний')
# print(out.name)
# inner = out.MyInner('внутренний', out)
# print(inner.inner_name)
# inner.inner_method()

# class Color:
#     def __init__(self):
#         self.name = 'Green'
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print('Name', self.name)
#
#     class LightGreen:
#         def __init__(self):
#             self.name = 'Light Green'
#
#         def display(self):
#             print('Name', self.name)
#
#
# outer = Color()
# outer.show()
# g = outer.lg
# g.display()

# class Computer:
#     def __init__(self):
#         self.name = "PC001"
#
#     class CPU:
#         def move(self):
#             return 'Intel'
#
#         def model(self):
#             return 'Core-i9'
#
#     class OS:
#         def system(self):
#             return 'Window'
#
#
# comp = Computer()
# print(comp.name)
# comp_os = Computer.OS()
# comp_cpu = Computer.CPU()
# print(comp_os.system())
# print(comp_cpu.move())
# print(comp_cpu.model())

# class Employee:
#     def __init__(self):
#         self.name = 'Employee'
#         self.intern = self.Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print('Name:', self.name)
#
#     class Intern:
#         def __init__(self):
#             self.name = 'Smith'
#
#         def display(self):
#             print('Name', self.name)
#
#     class Head:
#         def __init__(self):
#             self.name = 'Alba'
#
#         def display(self):
#             print('Name', self.name)
#
# outer = Employee()
# outer.show()

# class Outer:
#     def __init__(self):
#         self.inner = self.Inner
#     def show(self):
#         print('Outer show')
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass
#         def show(self):
#             print('inner show')
#
#         class InnerClass
#             def show(self):
#                 print('InnerClass show')
#
# o = Outer
# o.show()
#
# i1 = o.inner


# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f'{self.__class__}: {self.name}'
#
#     def __str__(self):
#         return  f'{self.name}'
#
#
# cat = Cat('Пушок')
# print(cat)

class Point:
    def __init__(self, *args):
        self.__coord = args

    def __len__(self):
        return len(self.__coord)


p = Point(2, 7, 10)
print(len(p))

# import math
#
#
# class Point:
#     __slots__ = ('x', "y", '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return  self.__length
#     @length.setter
#     def length(self):
#         self.__length = value
#
#
# p = Point(10, 12)
# print(p.length)

# class Point:
#     __slots__ = ('x', "y")
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# p = Point(1, 2)
# p2 = Point2D(1, 2)
# print('p = ',p.__sizeof__())
# print('p2 =', p2.__sizeof__() + p2.__dict__.__sizeof__())

# class Point:
#     __slots__ = ('x', "y")
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = 'z'
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
# pt = Point(1, 2)
# pt3 = Point3D(10, 20, 30)
# # pt3.z = 30
# print(pt3.x, pt3.y, pt3.z)
# print(pt3.__dict__)
