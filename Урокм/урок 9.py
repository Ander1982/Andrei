
# s = frozenset (i )

# словарь (dict)
# lst = {'one': 1, 'two': 2, 3: 0}
# print(lst)
# print(lst['one'])
# print(lst[3])

# d ={'one': 1, 'two':2, 3: 0}
# print(d)
# d1 = dict({'one': 1, 'two':2, 3: 0})
# d2 = dict(one=1, two=2)

# users = [('a', 'b'), ['c', 'd'] ,['e', 'f']]
# print(users)
# d_users = dict(users)
# print(d_users)
# lst = list(d_users)
# print(lst)

# d = {i: i ** 2 for i in range(7)}
# print(d)
# print(d[4])
# d[4] = 20
# print(d)

# d = {0: 'text', 'one': 1, (1, 2.3): 'kortehc', 2: [2, 3, 7, 6], True: 2, 5: 9}
# print(d)
# print((d[(1, 2.3)]))
# print(d[2][1])
# print('one' in d)
# del  d[0]

# d ={'one': 1, 'two':2, 'three': 3}
# for i in d:
#     print(i, d[i])

# key = 'two'
# if key in d:
#     del d[key]
# key = 'four'
# try:
#   del d[key]
# except KeyError:
#     print('')
# print(d)

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# print(d)
# r = 1
# for key in d:
#     r *= d[key]
# print(r)

# d = {i: input('->') for i in range(1, 5)}
# # d[1] = input('->')
# # d[2] = input('->')
# # d[3] = input('->')
# # d[4] = input('->')
# print(d)
# d1 = int(input('Какой элемент удалить: '))
# del d[d1]
# print(d)

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core i5-40R', 3, 8500],
#     '3': ['AAMD T-4330', 6, 3700],
#     '4': ['Pent FG480', 8, 2100],
#     '5': ['Core-i3-4330', 9, 6400],
# }
# for i in goods:
#     print(i, ')', goods[i][0], ' - ', goods[i][1], ' шт. по ', goods[i][2], 'руб', sep='')

# while True:
#     n = input('№: ')
#     if n != '0':
#        k = int(input('Количество: '))
#        goods[n][1] += k
#     else:
#         break
#
# for i in goods:
#     print(i, ')', goods[i][0], ' - ', goods[i][1], ' шт. по ', goods[i][2], 'руб', sep='')

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# print(d.keys()) #список ключей
# # print(d.values())#
# print(d.items())
# for i in d.values():
#     print(i)
# for i, j in d.items():
#     print(i, j)

# print(list(d.values()))
# print(tuple(d.items()))

# d = {'a': 1, 'b': 2, 'c': 3}
# d2 = d.copy()
# print(d)
# print(d2)
# d.update({'r': 7, 't': 9})
# print(d)

# x = {'a': 1, 'b': 2,}
# y = {'b': 3, 'c': 4,}
# z = x.copy()
# z.update(y)
# print(z)
# z = x | y
# print(z)

d = {'a': 1, 'b': 2, 'c': 3}
# # # d.clear()
# # # print(d)
# i = d.pop('b')
# # print(i)
# print(d)
# i = d.popitem()
print(d)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# new_d = dict()
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')

# new_d = {'name': d.pop('name'),'salary': d.pop('salary' }# другой вариант

# print(new_d)

# a = {
#     'first':{
#         1: '1',
#         2: '2',
#         3: '3'
#     },
#     'second': {
#         4: '4',
#         5: '5'
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, ':', a[x][y], sep='')