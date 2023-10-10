# n = int(input('Введите количество ворон (0- 9)'))
# if 0 <= n <= 9:
#     print("На ветке", end=" ")
#     if n == 1:
#         print("ворона")
#     elif 2 <= n <= 4:
#         print("Вороны")
#     else:
#         print("ворон")
# else:
#     print('Ошибка ввода')

# password = 'admin'

# match password:

# day = 'понедельник'
# time = 9
#
# match day:
#     case 'понедельник' |  'Вторник' if 9 <= time <= 16:
#         print('Раб')
#     case 'Суббота' | 'воскресенье':
#         print('вых')
#     case _:
#         print('Такого дня недели не существует')

# a, b = 10, 20
# min = a if a < b else b
# print(min)

# a, b = 10, 20
# print('a == b' if a == b else 'a > b' if a > b else 'b > a')

# a, b = 3, 1
# print('на ноль делить нельзя' if b ==  0 else a / b)

# try:
#     n = int(input('Введите целое число'))
#     print(n * 2)
# except ValueError:
#     print('уй')

# try:
#     n = int(input('первое'))
#     m = int(input('второе'))
#     print( n / m)
# except (ValueError, ZeroDivisionError):
#     print('нельзя')
# else:
#     print('все ок')
# finally: # влюбом случае выводит
#     print('конец')

# n = input('введитете первое число')
# m = input('Введите второе число')
#
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)

# i = 0
# while i < 5:
#     print('i=', i)
#     i += 1

# i = 10
# while i < 5:
#   print('i=', i)
#   i -= 1

# n = int(input('Введите количество символов'))
# i = 0
# while i < n:
#     print('*', end='')
#     i += 1

# n = int(input('Введите количество символов'))
#
# while 0 < n:
#     print('*', end='')
#     n -= 1

# print('*' * 4)

# a = int(input('начало диапазона:'))
# b = int(input('конец диапазона:'))
# res = 0
# while a <= b:
#     if a % 2:       # a % 2 != 0:
#         res += a
#         print(a)
#     a += 1
#
# print('сумма целых нечетных чисел:', res)

# n = input('Введите целое число:')
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print('Число не целое')
#         n = input('Введите целое число:')
# if n % 2 == 0:
#     print('Четное число')
# else:
#     print('Нечетное')

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=' ')
#     if i == 5:
#         break
#     i += 1
# print('\nЦикл завершен')

# i = 0
# while True:
#     print(i, end=' ')
#     if i == 5:
#         break
#     i += 1


# res = 1
# while True:
#     n = int(input('Введите число:'))
#     if n == 0:
#        break
#     res *= n
# print(res)

# i = 0
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print('Цикл окончен, i =', i)
