
# a = ['one', 1, 2, 3, 'two', 10, 20, 'three',15, 36, 60, 'four', -20 ]
# s = dict()
# n = None
# for i in a: #1
#     if type(i)== str:
#         s[i] =[] # s['one] = []
#         n = i # n = 'one'
#     else:
#         s[n].append(i) # s['one'] = [1,2,3]
#
# print(s)

# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# s = list(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d)
# print(s)

# a = ['dec', 'jan', 'feb']
# b = [12, 1, 2]
# f = {k: v for k, v in zip(a, b)}
# print(f)

# a = [1, 2, 3]
# c = [4.0, 8.5, 9.4]
# d = ['a', 'b', 'c']
# b = list(zip(a, c, d))
# print(b)

# dict_one = {'name': 'Igor', 'last_name': 'Doe', 'Job': 'Consult'}
# dict_two = {'name': 'Ira', 'last_name': 'Smit', 'Job': 'manedfer'}
# for (k1, v1), (k2, v2)  in zip(dict_one.items(), dict_two.items()):
#     print(k1 , v1)
#     print(k2, v2)

# two = [(1, 'a'), (2, 'b'), (3, 'c'), ('d', 7)]
# a, b = zip(*two)
# print(a)
# print(b)

# a = {'ap': 0.4, 'ora': 0.35}
# b = {'ber': 0.8, 'vod': 1.01}
# print({**a, **b})

# s = ['red', 'blue', 'green']
# j = 1
# for j, i in enumerate(s, 1):
#     print(j, ') ', i, sep='')
#     # j += 1

# def func(*args):
#     return args
#
# print(func())

# def summa(*param):
#     r = 0
#     for i in param:
#         r += i
#     return r
#
# print(summa(1, 2, 3, 5))
# print(sum (1, 2, 3, 5))

# def ch(*args):
#     averange = sum(args) / len(args)
#     print('среднее арифметическое:', averange)
#     r = []
#     for num in args:
#          if averange > num:
#              r.append(num)
#     return r
#
# print(ch( 1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))

# def func(a, *args):
#     return a, args
#
# print(func(5))
# print(func(5, 6, 7, 9))

# def print_scores(student, *scores):
#     print('student:', student, end=' :')
#     for score in scores:
#         print(score, end=' ')
#     print()
#
# print( print_scores('Vas', 100, 98, 45, 68))
# print( print_scores('Ras', 86, 8))

# def func(**kwargs):
#     for k, v in kwargs.items():
#         print(k, 'is', v)
#
# func(na='dfc', se='dd', age=65, cjn='rus')
# func(na='bjk', se='vv', age=165, cjn='rus', tel=788887)


# name = 'Tom'
# def hi():
#     global name
#     name = 'Sam'
#     global sername
#     sername = 'Johnson'
#     print('hie', name, sername)
#
#
# def bay():
#     print('good bay', name, sername)
#
# hi()
# bay()

# i = 5
#
# def func(arg=i):
#     print(arg)
#
# i = 6
# func()

# x = 6
# def func(a):
#     x = 2
#     def inner():
#        return  a + x
#     return inner()
#
# print(func(3))

# import builtins
#
# names = dir(builtins)
# for i in names:
#     print(i)

# def outer(who):
#     who = 'al'
#
#     def inner():
#         print('hello', who)
#
#     inner()
#
# outer('world')

# def f1():
#     a = 6
#
#     def f2(b):
#         a = 4
#         print('сумму:', a + b)
#
#     print('a =', a)
#     f2(4)
#
# f1()

# x = 25
# t = 0
#
# def fn():
#     global  t
#     a = 30
#     def inner():
#         nonlocal a
#         a = 35
#         print('a:', a)
#     inner()
#     t = a
# fn()
# c = x + t
# print(c)


# def f1():
#     x = 25
#
#     def fn2():
#         x = 33
#
#         def f3():
#             x = 55
#
#         f3()
#         print(fn2('x2', x))
#
#     fn2()
#     print(f1('x1', x))
#
# f1()

# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
# print(outer(2, 3, -1, 4))




