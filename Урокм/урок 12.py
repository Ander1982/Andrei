
# b = [66, 90, 59, 76, 60, 88, 76, 81, 65]
# r = list(filter(lambda s: s > 75, b))
# # r = list(filter(lambda s: (s > 75) and s < 80, b))
# print(r)

# Декоратор
# def hello():
#     return 'hello "nellow"'
#
# def super_f(func):
#     print('hello " super_func')
#     print(func())
#
# super_f(hello)

# def hello():
#     return 'hello "nellow"'
#
# test = hello
# print(test())
# print(hello())


# def my_decorator(func):
#     def wrad():
#         print('code befor')
#         func()
#         print('code after')
#     return  wrad
#
# def func_test():
#     print("Hello 'func_test'")
#
# test = my_decorator(func_test)
# test()

# def my_decorator(func):
#     def wrad():
#         # print('code befor')
#         func()
#         # print('code after')
#     return  wrad
#
# @my_decorator
# def func_test():
#     print("Hello 'func_test'")
#
# func_test()

# def bold(fn):
#     def wrap():
#         return '<b>' + fn() + '<b>'
#
#     return wrap
#
# @bold
# def hello():
#     return  'text'
#
# print(hello())

# def f(fn):
#     c = 0
#     def wrap():
#         nonlocal c
#         c += 1
#         fn()
#         print('Вызов:', c)
#
#     return wrap
#
#
#
# @f
# def hello():
#     print('hello')
#
# hello()
# hello()
# hello()

# def cnt(fn):
#     c = 0
#     def wrap():
#         nonlocal c
#         c += 1
#         fn()
#         print('Вызов функции:', c)
#
#     return wrap
# @cnt
# def hello():
#     print('Hello')
#
# hello()
# hello()
# hello()

# def arg_dec(fn):
#     def wrap(a1, a2):
#         print(a1, a2)
#         fn(a1, a2)
#
#     return wrap
#
# @arg_dec
# def print_full_name(f, l):
#     print('Меня зовут', f, l)
#
# print_full_name('Ira', 'Rez')

# def arg_dec(fn):
#     def wrap(*args, **kwargs):
#         print('args:>>', args)
#         print('kwargs:>>>', kwargs)
#
#         fn(*args,**kwargs)
#     return wrap
# @arg_dec
# def print_full_name(a, b, c, study='PYTHON'):
#     print(a, b, c, 'изучают', study, '\n')
# print_full_name('Bor', 'Elz','Swet', study='js')
# print_full_name('Djk', 'der','sqw')


# def decor(arg1, arg2):
#     def ards_dec(fn):
#         def wrap(x, y):
#             print(arg1, x, arg2, y, '=', end=" ")
#             fn(x, y)
#         return  wrap
#     return ards_dec
#
# @decor('суммы', "+")
# def s(a, b):
#     print(a + b)
# s(5, 2)
#
# @decor('разность', '-')
# def r(a, b):
#     print(a - b)
# r(5, 2)

# def mult(arg):
#     def outer(func):
#         def wran(*args, **kwargs):
#             return arg * func(*args, **kwargs)
#         return wran
#     return outer
#
# @mult(3)
# def return_n(n):
#     return n
# print(return_n(5))

# def typed(*args, **kwargs):
#     def outer(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError('неверный тип данных')
#
#             for k in kwargs:
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     raise TypeError('неверный тип данных', f_kwargs[k])
#
#             return fn(*f_args, **f_kwargs)
#         return wrap
#     return outer
#
# @typed(int, int, int)
# def t(x, y, z):
#     return x * y * z
#
# # print(t(2, 4, 5))
# # print(t(3, 6, '!'))
#
#
# @typed(str, str, str)
# def t2(x, y, z):
#     return x + y + z
# # ##
# # print(t2('hello', 'world', '!'))
# # print(t2(6, 4, 2))
#
# @typed(str, str, z=int)
# def t3(x, y, z='hello!'):
#     return (x + y) * z
#
# # print(t3('hello', 'world', z='5'))
# print(t3('hello', 'world', '!'))

#Префиксы

# r

# print('C:\folder\file.txt')
# print('C:\\folder\\file.txt')
# print(r'C:\folder\file.txt')
# print(r'C:\folder\file.txt' + '\\')
# print(r'C:\folder\file.txt\\'[:-1])

#f

# name = 'Dima'
# age = 25
# print(f'меня зовут {name}. мне {age} лет.')
# print(f'число: { round( 10 / 3, 2)}')
# print(f'число: {10 / 3:.2f}')