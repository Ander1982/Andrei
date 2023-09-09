# 1 Вариант
class Square:
    count = 0

    def __init__(self):
        Square.count

    @staticmethod
    def get_count():
        return Square.count

    @staticmethod
    def area_of_triangle(a, b, c):
        Square.count += 1
        p = 0.5 * (a + b + c)
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return s

    @staticmethod
    def area_of_triangle_2(a, b):
        Square.count += 1
        s = (a * b) / 2
        return s

    @staticmethod
    def area_of_rectangle(a, b):
        Square.count += 1
        s = a * b
        return s

    @staticmethod
    def area_of_the_square(a):
        Square.count += 1
        s = a * a
        return s


s1 = Square()
s2 = Square()
s3 = Square()
s4 = Square()
print('Площадь треугольника по формуле Герона:', s1.area_of_triangle(3, 4, 5))
print('Площадь треугольника через основание и высоту:', s2.area_of_triangle_2(6, 7))
print('Площадь квадрата:', s3.area_of_rectangle(2, 6))
print('Площадь прямоугольника:', s4.area_of_the_square(7))
print('Количество подсчетов площади:', Square.get_count())


# Вариант № 2 недостаток данного варианта, что подсчет ведется сколько формул в классе.
class Square:
    count = 0

    def __init__(self):
        Square.count

    @staticmethod
    def get_count():
        return Square.count

    @staticmethod
    def area_of_triangle(a, b, c):
        Square.count += 1
        p = 0.5 * (a + b + c)
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return s

    @staticmethod
    def area_of_triangle_2(a, b):
        Square.count += 1
        s = (a * b) / 2
        return s

    @staticmethod
    def area_of_rectangle(a, b):
        Square.count += 1
        s = a * b
        return s

    @staticmethod
    def area_of_the_square(a):
        Square.count += 1
        s = a * a
        return s


s1 = Square()
print('Площадь треугольника по формуле Герона:', s1.area_of_triangle(3, 4, 5))
print('Площадь треугольника через основание и высоту:', s1.area_of_triangle_2(6, 7))
print('Площадь квадрата:', s1.area_of_rectangle(2, 6))
print('Площадь прямоугольника:', s1.area_of_the_square(7))
print('Количество подсчетов площади:', Square.get_count())