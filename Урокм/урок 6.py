
# a = [1, 2, 3]
# # b = a
# b = a.copy()
# print(a)
# print(b)
# a.append(20)
# print(a)
# print(b)
# b.append(30)
# print(a)
# print(b)
#

# a = [1, 2, 3]
# a.reverse() # развернуть элементы
# print(a)
#
# s = [3, 8, 2, 7, 0, 1]
# s.sort() # сортировка по возрастанию по умолчанию
# print(s)
# s.sort(reverse=True)
# print(s)

# s2 = ['Виталий', 'Фaнна', 'Анна']
# print(s2)
# s2.sort(key=len)
# print(s2)
# s2.sort(key=len, reverse=True)
# print(s2)

# s = [5, 8, 9, 5, 3]
# s.sort()
# print(s)
# s2 = [5, 8, 9, 5, 3]
# s3 = sorted(s2)
# print(s2)
# print(s3)

# генерация случайных чисел
# import  random
# #
# #
# print(random.random())
# print(random.randint(0, 9)) #
# # print(random.randrange(1, 9, 1)) # начало, конц, шаг конец не включает

from random import *
# print(random())
# print(randint(0, 9)) #
# print(randrange(1, 9, 1))
# print(uniform(10.5, 12.6))
# print(round(uniform(10.5, 12.9), 2))

# city = ['моск', 'киев', 'пол']
# print(choice(city))
#
# s = [3, 7, 9, 10]
# # print(choice(s))
# print(choices(s))
# print(choices(s, k=2))

# a = [randint(0, 9) for i in range(10)]
# print(a)


# lst = [2, 5, 7, 2, 89, 23]
# print(len(lst))
# print(min(lst))
# print(max(lst))
# print(sum(lst))

# a = [randint(0, 100) for i in range(10)]
# print(a)
# m = max(a)
# print('Max:', m)
# a.remove(m)
# a.insert(0, m)
# print(a)

# a = [randint(0, 100) for i in range(10)]
# print(a)
# m = min(a)
# print('Min:', m)
# ind = a.index(m)
# print(ind)
# # del a[:ind]
# # print(a) или
# b = a[ind:]
# print(b)

# x = list('12dfyuyv')
# print(x)
# print('a' in x)
# print('a' not in x)

# l = []
# if not l:
#     print('Cписок пустой')
#
# print(bool(l))
#
# n1 = int(input('Введите размер списка 1'))
# n2 = int(input('Введите размер списка 2'))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# print('список 1', a)
# print('список 2', b)
# c = a + b
# print('список № 3:', c)

# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print('Третий список', c)
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#        c.append(a[i])
# print('Третий список', c)

# c = [min(a), min(b), max(a), max(b)]
# print('Третий список', c)

m = [
    [1, 2, 3, 4],
    [5, 6, 6, 7],
    [ 6, 8 , 9]
]
print(m)
print(m[1][2])

# s = ['hell', 2]
# print(s[0][1])

# for r in range(len(m)):
#     print(m[r])
#     for c in range(len(m[r])):
#        print(m[r][c], end='\t\t')
#     print()
# #
# for r in m:
#     for x in r:
#         print(x, end='\t\t')
#     print()

# w, h = 5, 4
# m = [[randint(1,30) for x in range(w)] for y in range(h)]
# for r in m:
#     for x in r:
#         print(x, end='\t\t')
#     print()

# w, h = 3, 4
# s = 0
# m = [[randint(-20,10) for x in range(w)] for y in range(h)]
# for r in m:
#     for x in r:
#         if x < 0:
#             s += 1
#         print(x, end='\t\t')
#     print()
#
# print('s =', s)