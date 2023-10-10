
# import math

# import math as m

# from math import ceil, floor
# num = ceil(3.2)

# from math import *
# num = ceil(3.2)

# import time

# sec = time.time()
# print(sec)
# locale = time.ctime()
# print(locale)
# r = time.localtime()
# print(r)
# print(r.tm_year)

# import time
# import locale

# locale.setlocale(locale.LC_ALL, 'ru')
# print(time.strftime('today is %B %d,%Y'))
# print(time.strftime('today is %B %d,%Y'))
# print(time.strftime('Сегодня  %d %m %Y'))

# print('Программа запустилась...')
# time.sleep(5)
# print()

# start = time.time()
# time.sleep(5)
# f = time.time()
# print('Время выполения программы', start - f, 'секунд')

# r = time.monotonic()
# time.sleep(5)
# f = time.monotonic()
# print('Время выполения программы', r - f, 'секунд')

# Срезы: списких[start: stop:step]
# s = [5, 9, 3, 7, 1, 8]
# print(s[0])
# print(s[0:-1:2])
# print(s[1:3])
# print(s[:3])
# print(s[::-1])

# s = [1, 2, 3, 4, 5, 6, 7]
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[0:1])
# print(s[6:])
# print(s[7:3:-2])
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# print(s)
# s[2:3] = []
# print(s)
# del s[:]
# print(s)

 # методы списков
# s = [1, 2, 3, 4, 5, 6, 7]
# s.append(99) # добавляет элемент в конец
# print(s)
# s.extend([8, 9, 10]) # несколько элементов
# print(s)
# s.extend('add')
# print(s)
# s.insert(0,100) # добавляет элемент в список, 1 индекс, 2 сам элемент
# print(s)

# s = []
# n = int(input('Количество элементов списка'))
# for num in range(n):
#     x = int(input('введите число'))
#     s.append(x)
# print(s)

# s = []
# n = int(input('введите число кратное 3'))
# for num in range(n):
#     x = int(input('введите число'))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print((x, 'нелится на 3 без остатков'))
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     if i in c:
#             continue
#     for j in b:
#         if i == j:
#             c.append(i)
# print(c)

# a = [1, 2, 3, 44, 55]
# b = [11, 22, 33]
# c = []
# if len(a) > len(b):
#     b, a = a, b
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
# print(c)

# a = [1, 2, 3, 4]
# b = [11, 22, 33]
# c = []
# # Добавить
# for i in range(len(a)):
#     c.append(a[i])
#     # c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
# print(c)

# s = [4, 0, 2, 0, 3, 6, 0, 0, 7]
# s.remove(0)  # удаляет первое значение
# print(s)
# # last = s.pop() # удаляет последний элемент
# # print(s)
# last = s.pop(-3) # удаляет по индексу элемент
# print(s)
# print(last)
# s.clear() # очищает список
# print(s)

# a = [int(input('->')) for i in range(int(input('n = ')))]
# print(a)
# print('введите идекс: ')
# k = int(input('k =  '))
# a.pop(k)
# print(a)

# s = [4, 0, 2, 0, 3, 6, 0, 0, 7]
# print(s)
# num = s.count(2) # считает количество элементов в списке
# print(num)
#
# ind = s.index(7) # возвращает индекс первого найденного числа
# print(ind)









