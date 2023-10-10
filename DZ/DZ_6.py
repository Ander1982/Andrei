import math

#Площадь прямоугольника

a = int(input('Введите высоту:>>'))
b = int(input('Введите длинну:>>'))
def triangle(х,y):
    print('Площадь прямоугольника =', х * y)
triangle(a, b)

# Площадь треугольника

a = int(input('Введите высоту:>>'))
b = int(input('Введите основание:>>'))
def triangle(h,y):
    print('Площадь треугольника =', h * y / 2)
triangle(a, b)

#Площадь круга

a = int(input('Введите радиус:>>'))
def circle(r):
    print('Площадь круга =', round(r ** 2 * math.pi, 2))
circle(a)




