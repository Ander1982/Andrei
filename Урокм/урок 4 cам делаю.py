
# i = 1
# while i < 4:
#     j = 1
#     while j < 16:
#         if j % 2 == 0:
#             print('-', end='')
#         else:
#              print('+', end='')
#         j += 1
#     print()
#
#     i += 1

# a = 10
# b = 100
#
#
# for i in range(a, b):
#     if i // 10 == i % 10:
#        print(i, end=' ')

# a = 16
# b = 4
# for i in range(b):
#     for j in range(a):
#         if i == 0 or j == 0 or i == b - 1 or j == a - 1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# a = [int(input('=>')) for i in range(int(input('Сколько элементов')))]
# s = 0
# for i in a:
#       if i > 0:
#        s += i
# print(s)

# a = list(range(21,41))
# print(a)
# j = 0
# s = 0
# for i in a:
#     if i % 2 == 0:
#         j += 1
#     else:
#         s += i
# print(j)
# print(s)

# import time
# a = [1, 2, 3, 4, 5, 6, 7]
# print(a[0:1])
# print(a[3:4])

# tuple1 = tuple('2535435456')
# print('картеж:', tuple1)
# solution = {}
# for i in tuple1:
#         if  i in solution:
#             solution[i] += 1
#             print('1:',solution[i])
#         else:
#              solution[i] = 1
#              print('2:',solution[i])
#
# for i, j in solution.items():
#     print(i, '=', j)

# a = 1
# b = 3
# c = {} | a
# с += a
# print(c)

# def ch(*args):
#     a = sum(args) / len(args)
#     print('средняя арифметическое', a)
#     r = []
#     for i in args:
#         if a < i:
#             r.append(i)
#     return r
#
#
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))