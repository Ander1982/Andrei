class Rectangle:

    def __init__(self, length, width):
        self.__length = self.__width = 0
        if Rectangle.__check_value(length) and Rectangle.__check_value(width):
            self.__length = length
            self.__width = width

    @staticmethod
    def __check_value(z):
        if isinstance(z, int) or isinstance(z, float):
            return True
        return False

    def set_data(self, length, width):
        if Rectangle.__check_value(length) and Rectangle.__check_value(width):
            self.__length = length
            self.__width = width
        else:
            print('Данные должны быть числом')

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_area(self):
        return self.__width * self.__length

    def get_perimeter(self):
        return (self.__width + self.__length) * 2

    def get_hypotenuse(self):
        return round(((self.__width ** 2) + (self.__length ** 2)) ** 0.5, 2)

    def get_picture(self):
        i = 0
        while i < self.__length:
            j = 1
            while j < self.__width:
                print("*", end='')
                j += 1
            print("*")
            i += 1





r1 = Rectangle(2, 3)
r1.set_data(3, 9)
print('Длинна прямоугольника:', r1.get_length())
print('Ширина прямоугольника:', r1.get_width())
print('Площадь прямоугольника:', r1.get_area())
print('Периметр прямоугольника:', r1.get_perimeter())
print('Длинна гипотенузы равна:', r1.get_hypotenuse())
r1.get_picture()
