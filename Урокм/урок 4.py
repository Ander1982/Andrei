
# i = 1
# while i < 5:
#     print('внешний цикл: i', i)
#     j = 1
#     while j < 4:
#         print('\tвторой цикл j:', j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j <10:
#         print(i, '*', j, '=', i*j, end='\t\t')
#         j += 1
#     print()
#     i += 1

# i = 1
# while i < 5:
#     j = 1
#     while j <= 10:
#         if i % 2 == 0:
#            print('+', end='')
#         else:
#            print('-', end='')
#         j += 1
#     print()
#     i += 1

# for i in 'Hello!':
#     print(i)

# for color in 'r', 'b', 'g':
#     print(color)

# for i in range(5):
#     print(i, end=" ")
#
# print()
#
# i = 0
# while i < 5:
#     print(i, end=' ')
    # i += 1

# a = int(input('введите целое число'))
# for i in range(1, a):
#     if a % i ==0:
#      print(i, end=' ')

# for i in range(10, 100):
#     if i % 10 == i // 10:
#       print(i, end=' ')

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print('Done!')

# for i in range(3):
#     print('+++')
#     for j in range(2):
#         print('---')

# w = int(input('введите ширину'))
# h = int(input('введите высоту'))
# w = 16
# h = 4
# for i in range(h):
#      for j in range(w):
#          if i == 0 or j == 0 or i  == h - 1 or j == w - 1:
#            print('*', end="")
#          else:
#              print(' ', end='')
#      print()

# a =[letter * 2 for letter in 'Hello!']
# print(a)

# nums = [8,8,4,6,7, 'Hello', 2.5]
# print(nums)
# print(type(nums))
# print(nums[-7])
# print(nums[3])
# nums[3] = 256
# nums[0] += 100
# print(nums)
# print(len(nums))

# s = []
# print(s)
# print(type(s))
#
# b = list()
# print(b)
# print(type(b))

# n = list(range(10))
# print(n)

# a = [0 for  i in range(5)]
# print(a)

# a = [i for  i in range(5)]
# print(a)

# a = [i * 3 for  i in 'list']
# print(a)

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)
# d = c * 3
# print(d)

# a = [0] * int(input('введите эл в списке'))
# # print(a)
# for i in range(len(a)):
#     print(i)
#     a[i] = input(' ->')
# print(a)

# a = [int(input(' >>>')) for i in range(int(input('введите эл в списке')))]
# print(a)

# a = ['один', 'два',' три']
# for i in range(len(a)):
#     print(a[i], end=' ')
#
# print()
#
# for el in a:
#     print(el, end=' ')

# a = [int(input(' >>>')) for i in range(int(input('n =')))]
# print(a)
# s = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         s += a[i]
# print('сумма отрицательных элеентов:' , s)

# for i in a:
#     if i < 0:
#         s += i
# print( ' eee o', s)

# n = list(range(21, 41))
# print(n)
# k = s = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]
#
# print('с1',k)
# print('c2', s)

# a = [int(input(' >>>')) for i in range(int(input('n =')))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#
#      print(a[i], end='')

