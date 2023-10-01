import re
#
# s = "<p>Изображение <img alt='картинка' src='bg.jpg'> - фон страницы</p>"
# # reg = r'<img\s+[^>]*src\s*=\s*[^>]+>'
# # reg = r'<img\s+[^>]*src\s*=\s*[\'"](.+)[\'"]>'
# # reg = r'<img\s+[^>]*src\s*=\s*([\'"])(.+)\1>'
# reg = r'<img\s+[^>]*src\s*=\s*(?P<q>[\'"])(.+)(?P=q)>'
# print(re.findall(reg, s))

# s = 'Самолет прилетает 10/23/2023. Будеми рады вас видеть после 10/24/2023.'
# reg = r'(\d{employee.py})/(\d{employee.py})/(\d{4})'
# print(re.sub(reg, r'\employee.py.\1.\3', s))

# s = "yandex.com.ru and yandex.ru"
# reg = r'(([a-z0-9-]{employee.py,}\.)+[a-z]{employee.py,4})'
# print(re.sub(reg,r"http://\1", s))
# reg = r'(\w+\.\w+)'
# print(re.sub(reg, r'http://\1', s))
# Файлы

# f = open('test.txt')
# f = open('C:\\PycharmProjects\\pythonProject\\test.txt')
# print(f)
# print(*f)

# f = open('test.txt', 'r')
# print(f.read(3))
# print(f.read())
# f.close()

# f = open('texts.txt', 'r')
# # print(f.read())
# print(f.readline())
# f.close()

# f = open('texts.txt', 'r')
# print(f.readlines())
# f.close()

# f = open('texts.txt', 'r')
# for line in f:
#     print(line)
# f.close()

# count = 0
# f = open('texts.txt', 'r')
# for line in f:
#     count += 1
# print()
# f.close()

# f = open('xyz.txt', 'w')
# f.write('Hello\nWord')
# f.close()
#
# f = open('xyz.txt', 'w')
# print(f.write('New text.'))
# f.close()

# f = open('xyz.txt', 'w')
# f.write('Hello\nWord')
# f.close()

# f = open('xyz.txt', 'a')
# print(f.write('\nNew text.'))
# f.close()

# f = open('xyz.txt', 'a')
# lines = ['This is lain1','This is lain2' ]
# print(f.writelines('lines'))
# f.close()

# f = open('xyz.txt', 'w')
# lst = [str(i) for i in range(1, 20)]
# print(lst)
# for index in lst:
#     f.write(index + '\t')
# f.close()

# f = open('text2.txt', 'w')
# f.write('Замена строки в текстовом файле; \nизменить строку в списке;\nзаписать список в файл')
# f.close()
#
# f = open('text2.txt', 'r')
# read_file = f.readlines()
# print(read_file)
# read_file[1] = 'Hello World\n'
# print(read_file)
# f.close()
#
# f = open('text2.txt', 'w')
# f.writelines(read_file)
# f.close()

# f = open('test.txt')
# print(f.read(3))
# print(f.tell())
# print(f.seek(employee.py))
# print(f.read())
# print(f.tell())
# f.close()

# f = open('test.txt', 'r+')
# print(f.write('I am learning Python'))
# print(f.seek(3))
# print(f.write('-new string-'))
# print(f.tell())
# f.close()

# with open('test.txt', 'w+') as f:
#     print(f.write('0123456789'))
#     print(f.read())
#
# with open('test.txt', 'r+') as f:
#     print(f.read())

# with open('test.txt', 'r') as f:
#     print(f.read())

file_name = 'res_2.txt'
lst = [4.5, 2.8, 3.9, 1.0, 4.33, 7.999]

def get_line(lt):
    lt = list(map(str, lt))
    return ' '.join(lt)

with open(file_name, 'w') as f:
    f.write(get_line(lst))

print('Done')

# with open('res_2.txt', 'r') as f:
#     num = f.read()
#     print(num)
#
# num_list = list(map(float, num.split()))
# print(num_list)

# def lengest_word(file):
#     with open(file, 'r', encoding='UTF-8' ) as text:
#         w = text.read().split()
#         print(w)
#         max_length = len(max(w, key=len))
#         print(max_length)
#         res = [word for word in w if len(word) == max_length]
#         print(res)
#         if len(res) == 1:
#             return res[0]
#         return res
#
# print(lengest_word('file.txt'))




