
# x = 10
# y = 5
# print(f'{x=}')
# print('x=', x, sep='')
# print(f'{x} * {y} / 2 = {x * y / 2 }')

# num = 74
# print(f'{{{{{num}}}}}')
# print(f'{{{{num}}}}')

# dir_name = 'my_doc'
# file_name = 'date.txt'
# print(fr'home\{dir_name}\{file_name}')

# s = '''Hello
#                world'''
# s1 = """Hello
#               world"""
# s2 = 'Hello \
#               world'
# print(s)
# print(s1)
# print(s2)
#
# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return  n ** 2
# print(square(5))
# print(square.__doc__)

# import math
# def cylinder(r, h):
#     '''
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     '''
#     return 2 * math.pi * r * (r + h)
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)

# print(ord('a'))
# print(ord('A'))
# print(ord('А')) # русская

# while True:
#     n = input('-> ')
#     if n != '-1':
#         print(ord(n))
#     else:
#         break

# s = 'Test string for me'
# arr = [ord(x) for x in s]
# print('ASCII коды:', arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print('Среднее арифметическое', arr)
# arr += [ord(x) for x in input('-> ')[:3] if ord(x) not in arr]
# print('количество элементов:', arr)
# print(arr.count(arr[-1]))
# arr.sort(reverse=True)
# print(arr)

# print(chr(97))

# a = 122
# b = 97
# if b > a:
#     a, b = b, a
# for i in range(b, a + 1):
#     print(chr(i), end=' ')

# for i in range(b, a + 1):
#     print(chr(i, end=' '))
# for i in range(a, b + 1):
# print(chr(i, end=' '))

from random import  randint

# s = 7
# l = 10
# min_a = 33
# max_a = 126
#
# def  random_password():
#     rand_len = randint(s, l)
#     r = ''
#     for i in range(rand_len):
#         rand_char = chr(randint(min_a, max_a))
#         r  += rand_char
#
#     return r
#
# print('Ваш случайный пароль:', random_password())

# s = 'hello, WORD! I am learning Python!'
# print(s.capitalize()) #первый букву в первый регистр
# print(s.lower()) # нижний регистр
# print(s.upper()) # верхний
# print(s.swapcase()) # меняет регистр
# print(s.title()) # первые слоа верхний

# print(s.count('h'))
# print(s.count('h', 1))
# print(s.count('h', 1, -4))

# print(s.find('Python'))
# print(s.find('Python', 0, 30))
# print(s.rfind('h'))#поиск с конца
# print(s.index('Python'))
# print(s.rindex('h'))

# s1 =  'I am learning Python. hello, WORD!'
# # s1 = s1[:s1.find('h')] + s1[s1.rfind('h') + 1:]
# # print(s1)
#
#
# print(s1.startswith('hello'))

# print('abc123' .isalnum())
# print('abcWW' .isalpha())
# print('123'.isdigit())
# print('abc766$$' .islower())
# print('ABC454#' .isupper())

# print('py' .center(10, '-'))
