
lst_1 = [int(input('Введите колличество элементов в списке')) for i in range(int(input('введите элементы в списке')))]
print('Список введенных элементов:', lst_1)

lst_2 = []
for i in lst_1:
    if i > 0:
        lst_2.append(i)
print('Список в котором остались только положительные элементы:',lst_2)

num = 0
for i in lst_2:
    if i > num:
        num = i

if num != 0:
    print('Наибольшее элемент списка:', num)
else:
    print('В новом списке отсутствуют элементы')



