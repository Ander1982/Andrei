
# # Функции
# def Hello(name, word): # аргумент
#     print('Hello')
#
#
# Hello('Iva', '344') # параметры

# def get_sum(a,b):
#     print(a + b)
# get_sum(2, 4)
# get_sum('adc', 'qwe')

# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end='')
#         else:
#             print(b, end='')
#
#
# symbol(9, '+', '-')
# symbol(7, 'X', '0')


# def get_sum(a,b):
#     return a + b
#
# n = 2
# m = 3
# r = get_sum(n, m)
# print(r)

# def add(x, y):
#     if x > y:
#         return x - y
#     return x + y
# a = int(input(' a = '))
# b = int(input('b = '))
# m = add(a, b)
# print('result:', m)

# def cube(a):
#     return a * a * a
# for i in range(1, 11):
#     print(i, 'кубе', cube(i))

# def change(lst):        1
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     return  lst
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['c', 'л', 'о', 'н']))

# def change(lst):
#     a = lst.pop() # последний элемент
#     b = lst.pop(0) # первый элемент
#     lst.append(b)
#     lst.insert(0, a)
#     return  lst
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['c', 'л', 'о', 'н']))

# def func(x, y):
#     if x > y:
#         return True
#     else:
#         return  False
# print(func(10, 5))

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if 'A' <= ch <= 'Z':
#             has_upper = True
#         elif 'a' <= ch <= 'z':
#             has_lower = True
#         elif '0' <= ch <= '9':
#             has_num = True
#
#     if len(password)>= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
# p = input('passvord: ')
# if check_password(p):
#     print('Good')
# else:
#     print('bed')

# def get_sum (a, b, c, d):
#     return a + b + c + d
#
# print(get_sum(1, 2, 3, 5)) # сколько аргументов столько вверху

# def get_sum (a, b=2, c=5, d=1):
#     return a + b + c + d
#
# print(get_sum(1, 2, 3, 5))
# n= 2
# print(get_sum(1, 2, c=n, 5))
# print(get_sum(1, 2,))
# print(get_sum(1, 2,  d=5))

# def set_param(c=20, s='-'):
#     for i in range(c):
#         print(s, end='')
#     print()
#
# set_param(10, '+')
# set_param(5, '*')
# set_param(15, '#')
# set_param(7)
# set_param()
# set_param(s='?')

# def digits_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_gigit = n % 10
#         if even and cur_gigit % 2 == 0:
#             s += cur_gigit
#         elif not even and cur_gigit % 2 !=0:
#             s += cur_gigit
#         n //= 10
#     return s
#
#
# print('сумма четных цифр:')
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
#
# print('сумма нечетных цифр:')
# print(digits_sum(9874023, even=False))
# print(digits_sum(38271, even=False ))
# print(digits_sum(123456789, even=False))

# def display_info(name, age):
#     print('Name:', name, '\nAge', age)
#
# display_info('Ira', 23)
# display_info(age=23, name='Ira')

# a = 5
# print(a, id(a))
# a = 6
# print(a, id(a))
#
# lst1 = [1, 2, 3]
# print(lst1, id(lst1))
# lst1.extend([4, 5, 6])
# print(lst1, id(lst1))

# a = 'qwe'
# b = 'qwe'
# a = 5
# b = 5
# print(a == b)
# print(a is b)
# print(id(a))
# print(id(b))