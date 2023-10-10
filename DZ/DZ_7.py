

# tuple1 = tuple(input('Введите элементы(цифры) кортежа:'))
tuple1 = tuple('2535435456')
print('картеж:', tuple1)
solution = {}
for i in tuple1:
    if i in solution:
        solution[i] += 1
    else:
        solution[i] = 1

for i, j in solution.items():
    print(i, '=', j)
