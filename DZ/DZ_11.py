
students = [
    {'name': 'Jennifer', 'final': 95},
    {'name': 'David', 'final': 92},
    {'name': 'Nikolas', 'final': 98}
]

res = sorted(students, key=lambda item: item['name'])
print('Отсортированный список студентов по именам:', res)
res = sorted(students, key=lambda item: item['final'], reverse=True)
print('Отсортированный список по итоговым оценкам в порядке убывания:',res)

nums = [3, 5, 7, 3, 9, 5, 7, 2]

a = list(map(lambda i: i ** 2, nums))
print('Возведение списка в квадрат:', a)
a = list(map(lambda i: i ** 3, nums))
# a = list(map(lambda t: t * 2, [2, 8, 12, 5, 10]))
print('Возведение списка в куб:', a)