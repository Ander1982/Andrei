
from random import *
print('Задача № 1')
lst_1 = 10
a = [randrange(0, lst_1)  for i in range(lst_1 * 10)]
c = []
for i in range(len(a)):
    if a[i] not in c:
        c.append(a[i])
print('Размер списка:', len(c))
print('Cписок из уникальных чисел', c)
print()
print('Задача № 2')


w = h = 6
m = [[randint(1,10) for x in range(w)] for y in range(h)]

for r in m:
    for x in r:
        print(x, end='\t\t')
    print()

j = [randint(1,10) for i in range(6)]
print(j)

m [0:1] = [j]
m [2:3] = [j]
m [4:5] = [j]

for w in m:
    for x in w:
        print(x, end='\t\t')
    print()