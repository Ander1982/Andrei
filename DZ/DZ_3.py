
i = int(input('Введите число от 1 до 99'))
if 1 <= i <= 99:
    if i == 1 or i % 10 == 1 and i != 11:
        print(i, 'копейка')
    elif 2 <= i <= 4 or 2 <= i // 10 <= 9 and 2 <= i % 10 <= 4:
        print(i, 'копейки')
    else:
        print(i, 'копеек')
else:
    print('Ошибка ввода')
