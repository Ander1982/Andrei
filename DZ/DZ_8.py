
a = {
    'John': {
        'N': 3056,
        'S': 8464,
        'E': 8441,
        'W': 2694
    },
    'Tom': {
        'N': 4832,
        'S': 6786,
        'E': 4737,
        'W': 3612
    },
    'Anne': {
        'N': 5239,
        'S': 4802,
        'E': 5820,
        'W': 1859
    },
    'Fiona': {
        'N': 3904,
        'S': 3645,
        'E': 8821,
        'W': 2451
    },

}

for x in a:
    print(x)
    for y in a[x]:
        print('\t', y, ':', a[x][y], sep='')

name = (input('введите имя продавца'))
region = (input('введите регион'))
print('Имя:', name)
print('Регион:', region)
print(a[name][region])
a[name][region] = int(input('Новое значение:',))
print(a[name])

