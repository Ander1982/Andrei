
# def elevator(n):
#     if n == 0:
#         print('Вы в подвале')
#         return
#     print('=>', n)
#     elevator(n - 1)
#     print(n, end=' ')
#
#
# n1 = int(input('На каком этаже Вы находится'))
# elevator(n1)

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
#
# print(sum_list(([1, 3, 5, 7, 9])))

# def sum_list(lst):
#
#
# print(sum_list(([1, 3, 5, 7, 9])))

# def to_str(n, base):
#     convert = '0123456789ABCDEF'
#     if n < base:
#         return  convert[n]
#     else:
#         return  to_str(n // base, base) + convert[n % base]
#
# print(to_str(254, 16))

# names = ['Adam',['Bob', ['Chet', 'Cat'], 'Bart', 'Bert'], 'Alex',['Bea','Bill'], 'Ann']
# print(names)
# print(names[0])
# print(isinstance(names[0], list))
# print(names[1])
# print(names[1], list)

# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
# print(count_items(names))

# def remove(text):
#     if not text:
#         return ''
#     if text[0] == '\t' or text[0] == ' ':
#         return remove(text[1:])
#     else:
#         return vte
#
# print(remove('  Hello\tWorld    '))


# Класс
# class Point:
#     x = 1
#     y = 1
#
# p1 = Point()
# print(p1.x)
# print(p1.y)
# p1.x = 10
# print(p1.x)
# print(type(p1))
# p2 = Point()
# print(p2.x)
#
# p1.z = 5
# print(p1.z)
#
# print(p1.__dict__)

# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#
# p1 = Point()
# p1.set_coord(5, 10)
# p2 = Point()
# # Point.set_coord(p1, 5, 10)
# print(p1.__dict__)
# p2.set_coord(20, 70)
# print(p2.__dict__)

class Human:
    name = 'name'
    birthday = '00.00.0000'
    phone = '00-00-00'
    country = 'country'
    city = 'city'
    address = 'address'

    def print_info(self):
        print('Персональные данные'.center(40, "*"))
        print(f'Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}'
              f'\nСтрана: {self.country}\nГород:{self.city}\nДомашний адрес:{self.address}')
        print('=' * 40)

    def input_info(self, first_name, birthday, phone, country, city, address):
        self.name = first_name
        self.birthday = birthday
        self.phone = phone
        self.country = country
        self.city = city
        self.address = address

    def set_city(self, value):
        self.city = value

    def get_sity(self):
        return self.city


h1 = Human()
print(h1.name)
h1.print_info()
h1.input_info('Юля', '23.07.1983', '34-87-90', 'Россия', 'Москва', ' ул.Гоголя')
h1.set_city('Владимир')
h1.print_info()
print(h1.get_sity())