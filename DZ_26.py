class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'{self.x}, {self.y}, {self.z}'

    def __add__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError('Правый операнд тип данных должен быть Point3D')
        return Point3D((self.x + other.x), (self.y + other.y), (self.z + other.z))

    def __sub__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError('Правый операнд тип данных должен быть Point3D')
        return Point3D((self.x - other.x), (self.y - other.y), (self.z - other.z))

    def __mul__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError('Правый операнд тип данных должен быть Point3D')
        return Point3D((self.x * other.x), (self.y * other.y), (self.z * other.z))

    def __truediv__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError('Правый операнд тип данных должен быть Point3D')
        return Point3D((self.x / other.x), (self.y / other.y), (self.z / other.z))

    def __eq__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError('Правый операнд тип данных должен быть Point3D')
        return self.x == other.x and self.y == other.y and self.z == other.z

    def get_result(self):
        return f"{self.x}, {self.y}, {self.z}"

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError('Ключ должен быть строкой')
        if item == 'x':
            return self.x
        elif item == 'y':
            return self.y
        elif item == 'z':
            return self.z
        return 'Неверный ключ'

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError('Ключ должен быть строкой')
        if not isinstance(value, int):
            raise ValueError('Значение должен быть целым числом')

        if key == 'x':
            self.x = value
        elif key == 'y':
            self.y = value
        elif key == 'z':
            self.z = value


c1 = Point3D(12, 15, 18)
c2 = Point3D(6, 3, 9)
print('Координаты 1-й точки:', c1)
print('Координаты 2-й точки:', c2)

c3 = c1 + c2
print(f'Сложение координат: ({c3.get_result()})')
c4 = c1 - c2
print(f'Вычитание координат: ({c4.get_result()})')
c5 = c1 * c2
print(f'Умножение координат: ({c5.get_result()})')
c6 = c1 / c2
print(f'Деление координат: ({c6.get_result()})')
if c1 == c2:
    print('Равенство координат:', True)
else:
    print('Равенство координат:', False)

print(f" x = {c1['x']}  x1 = {c2['x']}")
print(f" y = {c1['y']}  y1 = {c2['y']}")
print(f" z = {c1['z']}  z1 = {c2['z']}")

c1['x'] = 20
print(f"Запись значения в координату х: {c1['x']}")
c2['x'] = 21
print(f"Запись значения в координату х: {c2['x']}")
c1['z'] = 22
print(f"Запись значения в координату z: {c1['z']}")
c2['y'] = 23
print(f"Запись значения в координату y: {c2['y']}")
