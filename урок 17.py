import re
# s = '05-03-1987 #  Дата рождения'
# print('Дата рождени:', re.sub('#.*','', s))
# print('Дата рождени:', re.sub('#.*','', s))
# print('Дата рождени:', re.sub('-','.', re.sub('#.*','', s)))
# s = "12 сентября 2023 год"
# req = r'\d{2,4}'
# print(re.findall(req, s))
# req = r'\d{2,4}'
# print(re.findall(req, s))

# s = '+7 499 456-45-78, +74994564578, 7(499) 456 45 78, 74994564578'
# # reg = r"\+?7\d{10}"
# # print(re.findall(reg, s))
# reg = r'\+?\d{11}'
# print(re.findall(reg, s))

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# reg = r'\w+\s\w+'
# reg = r'^\w+\s\w+'
# reg = r'\w+\.$'
# print(re.findall(reg, s))

# def validate_login(name):
#     return re.findall(r'^[A-za-z_-]{3,16}$',name)
#
# print(validate_login("Python_master"))
# print(validate_login("%%Py"))
# print(validate_login("Py%%%"))


# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'\w+', '12 + й', flags=re.ASCII))

# text = 'hello word'
# print(re.findall(r"\w+", text, flags=re.DEBUG))

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта"
# reg = 'я'
# print(re.findall(reg, s, re.IGNORECASE))

# text = """
# one
# two
# """
# # print(re.findall(r'one.\w+', text))
# # print(re.findall(r'one.\w+', text, flags=re.DOTALL))
#
# print(re.findall('one$', text))
# print(re.findall('one$', text, flags=re.MULTILINE))
#
# print(re.findall('''[a-z.-]+@[a-z.-]+''', 'test@mail.ru'))
# print(re.findall('''[a-z.-]+@[a-z.-]+''', 'test@mail.ru', flags=re.VERBOSE))

# text = """Python,
# python,
# PYTHON"""
# reg = '(?im)^python'
# print(re.findall(reg, text))

# text = "<body>Fgdhfgjghk ghkkgk gjkjghk</body>"
# # # print(re.findall('<.*>', text))
# # print(re.findall('<.*?>', text))
# print(re.findall('<b[^>]*>', text))


# s = "<p> Изображение <img src='bg.jpg'> - фон страницы</p>"
# # reg = r'<img.*?>'
# # reg = r'<img[^>]*>'
#
# s = "<p>Изображение <img alt='картинка' src='bg.jpg'> - фон страницы</p>"
# reg = r'<img\s+[^>]*src\s*=\s*[^>]+>'
# print(re.findall(reg, s))

# s = "Петр, Ольга и Виталий отлично участся!"
# reg = "Петр|Ольга|Виталий|Николай"
# print(re.findall(reg, s))

s = "int = 4, float = 4/0, double = 8.0f"
# reg = r"\w+\s*=\s*\d+[.\w+]*"
# reg = r"(?:int|double)\s*=\s*\d+[.\w+]*"
# print(re.findall(reg, s))
# reg = r'<img.*?>'
# print(re.findall(reg, s))

# # s = '127.0.0.1'
# s = '192.168.255.255'
# reg  = r'(?:\d+\.{1,3}){3}\d{1,3}'
# print(re.findall(reg, s))

# s = 'World2016, Ps5, AI6'
# # reg = r'\w+'
# reg = r'[a-z]+\d+'
# print(re.findall(reg, s, re.I))

# s = '21-08-2023'
# reg = r'(0[0-9]|[12][0-9]|3[0-1])-(0[1-9]|1[0-2])-(19|20[0-99)]'
# print(re.findall(reg, s))

text = """
Москва
Самара
Калининград
"""
count = 0

def city_finde(m):
    global count
    count += 1
    return f'<option{count}>{m.group(1)}</option>\n'

print(re.sub(r'\s*(\w+)\s*', city_finde, text))