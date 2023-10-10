
# Замыкание

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
# i = outer(5)
# print(i(10))
#
# j = outer(6)
# print(j(20))
#
# print(outer(4)(6))

# def f1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#     def f2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + ' new'
#         return a, b, c
#     return f2
# f = f1()
# print(f())

# def f(city):
#     s = 0
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
# r = f('Москва')
# r()
# r()
# r2 = f('Сочи')

# students = {
#     'ali': 98,
#     'bob': 67,
#     'Chris': 85,
#     'd': 75,
#     'e': 54,
#     'f': 35,
#     'g': 69
# }
#
# def make(lower, upper):
#     def inner(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return inner
#
# bal_a = make(80, 100)
# bal_b = make(70, 80)
# bal_c = make(50, 70)
# bal_d = make(0, 50)
# print(bal_a(students))
# print(bal_b(students))
# print(bal_c(students))
# print(bal_d(students))

# def f(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return  a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         print()
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
# obj1 = f(5,2)
# print(obj1.add())
# print(obj1.sub())
# print(obj1.mul())

# анонимные функции (lambda - выражение)

# def s(x, y):
#     return x + y
#
# print(s(1, 2))
#
# print((lambda x, y : x + y)(1, 2))
#
# a = lambda x, y : x + y
# print(a(1, 2))

# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
# for i in c:
#     print(i('abc_'))

# def outer(n):
#     def inner(x):
#         return x + n
#
#     return inner
# f = outer(42)
# print(f(1))
#
# def outer1(n):
#     return lambda x: x + n
# f1 = outer1(42)
# print(f1(1))
#
# outer2 = lambda n: lambda x: x + n
#
# f2 = outer2(42)
# print(f2(1))
#
# print((lambda n: lambda x: x + n)(42)(1))

# print((lambda a: lambda b: lambda c: a + b + c)(2)(4)(6))

# d = { 'a': 10, 'c': 15, 'b': 4}
# q = list(d.items())
# print(q)
# q.sort()
# print(q)
# d1 = dict(q)
# print(d1)
# q.sort(key=lambda i: i[1])
# print(q)
# q.sort(key=lambda i: i[1], reverse=True)
# print(q)

# players = [
#     {'name': 'Ant', 'last name': 'Bir', 'raiting': 9},
#     {'name': 'Ali', 'last name': 'Bor', 'raiting': 10},
#     {'name': 'Fed', 'last name': 'Cid', 'raiting': 4},
#     {'name': 'Maik', 'last name': 'Cem', 'raiting': 6},
# ]
#
# r = sorted(players, key=lambda item: item['last name'])
# print(r)
# r = sorted(players, key=lambda item: item['raiting'])
# print(r)
# r = sorted(players, key=lambda item: item['raiting'], reverse=True)
# print(r)

# a = [(lambda  x, y: x + y),(lambda  x, y: x - y), (lambda  x, y: x * y), (lambda  x, y: x / y)]
# b = a[1](12, 5)
# print(b)

# d = {
#     1: lambda: print('понедельник'),
#     2: lambda: print('вторник'),
#     3: lambda: print('среда'),
#     4: lambda: print('четверг'),
#     5: lambda: print('пятница'),
#     6: lambda: print('суббота'),
#     7: lambda: print('воскресенье'),
# }
# d[2]()

# map(func, iter), filter(func, iter)

# def mult(t):
#     return  t * 2
#
# lst = [2, 8, 12, 5, 10]
#
# a = list(map(mult, lst))
# print(a)
# a = list(map(lambda t: t * 2, lst))
# a = list(map(lambda t: t * 2, [2, 8, 12, 5, 10]))

# t = (2.88, - 1.75, 100.55)
#
# t2 = tuple(map(lambda x: int(x), t))
# print(t2)
# t3 = tuple(map(int, t))
# print(t3)

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# r = list(map(lambda x, y: (x, y), st, num))
# print(r)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# l3 = list(map(lambda x, y: x + y, l1, l2))
# print(l3)

# t = ('adcg', 'rrfgg', 'ddhfyy', 'der', 'opp')
# t1 = tuple(filter(lambda s: len(s) == 3, t))
# print(t1)