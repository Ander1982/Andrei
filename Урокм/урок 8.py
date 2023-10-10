
# кортеж#
# lst = [10, 20, 30]
# tpl = (10, 20, 30)
#
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = 4, 5, 6, 8
# b = 4,
# print(a)
# print(b)

# a = tuple(('hell' 'hi'))
# print(a)

# a = tuple((2, 5, 7, 9, 8))
# print(a)
# print(a[1])
# print(a[1:3])

# s = tuple(input('=>') for i in range(5))
# print(s)

# from  random import  randint
# s = tuple(randint(0,10) for i in range(5))
# print(s)

# s = tuple(2 ** i for i in range(1, 13))
# print(s)

# t1 = tuple('hello')
# t2 = tuple('world')
# t3 = t1 + t2
# print(t3)
# for i in t3:
#     print(i, end='')
# print(t3.count('l'))
# print(t3.index('l', 3))
# ch = 'a'
# # if ch in t3:
#     print(t3.index(ch))
# else:
#     print('no')
#
# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.inde
#         else:
#             return  tpl[]
#     else:
#         return ()
#

# print(slicer(1, 2, 3), 8)
# print(slicer(1, 8, 3, 4, 8, 8, 9, 2), 8)
# print(slicer(1, 2, 8, 5, 1, 2, 9), 8)

# from random import randint
#
# def ran(a, b):
#     return tuple(randint(a, b) for i in range(10))
#
# tpl_1 = ran(0, 5)
# tpl_2 = ran(-5, 5)
# print(tpl_1)
# print(tpl_2)
# tpl_3 = tpl_1 + tpl_2
# print(tpl_3)
# print(tpl_3.count(0))

# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello'])
# t[4][0] = 'new'
# print(t)
# t[4].append('hi')
# print(t)
# del t[4][0]
# print(t)

t = (1, 2, 3)
x, y, z = t # распаковка картежа
print(x, y, z)

# def get_user():
#     name = 'Tom'
#     age = 22
#     is_marride =False
#     return  name, age, is_marride
#
# user = get_user()
# print(user)
# n, year, marride = get_user()
# print(n, year, marride)

# t = (1, 2, 3) # удалить
# del t
# print(t)

# t = (1, 2, 3)
# t = list(t)
# t.append(50)
# print(t)
# t = tuple(t)
# print(t)

# coutries = (
#     ('ger', 80.2, (('berlin', 3.326), ('gam', 1.718))),
#     ('fra', 66, (('paris', 2.2), ('marsel', 1.6))),
# )
# # print(coutries)
# for country in coutries:
#     country_name, country_population, cities = country
#     print('\nСтрана:', country_name, '.Население: ', country_population)
#     for city in cities:
#         city_name, city_population = city
#         print('\tГород', city_name, 'Население :', city_population)

# множество = set

# s = {'banana', 'apple', 'orange'}
# print(s)
# print(type(s))

# s = set()
# print(a)
# print(type(a))

# s = {i * i for i in range(10)}
# print(s)
# print(64 in s)

# s = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# # a = {i for i in s if 'a' in i}
# # a = {'A' + i[1:] if i[0] == 'a' else  'B'  + i[1:] for i in s}
# a = {'A' + i[1:] if i[0] == 'a' else  'B'  + i[1:] for i in s if i[1] == 'c'}
# print(a)

# a = {'Tom', 'BoB', 'Alice'}
# a.add('Sam')
# print(a)
# a.remove('Tom')
# # a.remove('Ann') #KeyError
# # print(a.pop())
# a.clear()
# print(a)

# a = {0, 1, 2, 3 }
# b = {4, 3, 6, 7}
# # c = a.union(b)
# c = a | b
# print(c)

# a1 = {1, 2}
# a2 = {3}
# a3 = {4, 5}
# a4 = {3, 2, 6}
# a5 = {6}
# a6 = {7, 8}
# a7 = {9,8}
# a = a1 | a2 | a3 | a4 | a5 | a6 | a7
# print(a)
# print(len(a))
# print(min(a))
# print(max(a))
