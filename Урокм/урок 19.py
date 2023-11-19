# text = 'Строка №1\nСтрока №employee.py\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n'
#
# with open('one.txt', 'w') as f:
#     f.write(text)

# read_file = 'one.txt'
# write_file = 'two.txt'
#
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace('Строка', 'Линия -')
#         fw.write(line)

# read_file = 'one.txt'
# write_file = 'two.txt'
# res = 'three.txt'
#
# with open(read_file, 'r') as fr, open(write_file, 'r') as fw, open(res, 'w') as res:
#     # f1 = fr.readlines()
#     # print(f1)
#     # f2 = fw.readlines()
#     # print(f2)
#     # f3 = f1 + f2
#     # res.writelines(f3)
#     for i, j in zip(fr,fw):
#         res.write(i[:-1] + '->' + j)

# Модуль ОS (OS.PATH)

import os


# print('Текущая директория', os.getcwd()) # путь к файлу
# print(os.listdir()) # список папок и файлов в текущей директроии
# print(os.listdir('..'))

# os.mkdir('folder1') #создать папку  при этом только одну( без путей)
# os.makedirs('nested/nested1/nested2') # может создвать вложенные папки
# os.mkdir('pop')
# os.remove('Work/11111.txt')# удалил файл
# os.remove('11111.txt')# удалил файл
# # os.rmdir('folder1')# удалить только пустую папку
# os.rename('xyz.txt', 'first.txt')#переименовать файл
# os.rename('first.txt', 'pop/first.txt')#переименовать файл b gthtvtcnbnm

# for root, dirs, files in os.walk('pop'):
#     print('Root:', root)
#     print('Subdirs:', dirs)
#     print('Files:', files)

# def remove_empty_dir(room_tree):
#     print(f'Удаление пустых директорий в папке {room_tree}')
#     print('-' * 50)
#     #
#     for root, dirs, files in os.walk(room_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f'Директория {root} удалена.')
#     print('-' * 50)
#
# remove_empty_dir('nested')

import os.path
# import time
# def dell_1(tree_1):
#     print(f'Удадение файлов в папках {tree_1}')
#     print('-' * 50)
#     for root, dirs, files in os.walk(tree_1):
#         # print('фыйл', files)
#         for d in dirs:
#         # print('dirs', d)
#             for f in files:
#                 # print('files', f)
#                 file_dell = os.path.join(root, d, f)
#                 print(file_dell)
#                     # os.remove(r'file_dell')
#         #
#     #         for f in d:
#     #               print('1>>>', f)
#     #
#     #             os.remove(os.path.join(f))
#     #     print(f'Файлы в директории {tree_1} удалены')
#     # print('-' * 50)
# dell_1('Work')

# dirs = ['Work\F1', r'Work\F2\F21']
# for d in dirs:
#     os.makedirs(d)

# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\f21': ['f211.txt', 'f212.txt']
# }
# for d, file in files.items():
#     for f in file:
#         file_path = os.path.join(d, f)
#         print(file_path)
#         open(file_path, 'w').close()
# #
# #
# files_with_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\f211.txt', r'Work\F2\f21\f211.txt']
# for file in files_with_text:
#     with open(file, 'w') as f:
#         f.write(f'Какой-то текст {file}')
# #
# def print_tree(root, topdown):
#     print(f'Обход {root} {"Сверху вниз" if topdown else "снизу вверх"}')
#     for root, dirs, files in os.walk(root, topdown=topdown):
#         print(root)
#         print(dirs)
#         print(files)
#     print('-' * 50)
#
# print_tree('Work', topdown=False)
# print_tree('Work', topdown=True)

# import time
# path = 'урок 40 .py'
# size = os.path.getsize(path)
# print(size // 1024, 'KB')
# ctime = os.path.getctime(path)
# print(time.strftime('%d.%m.%Y, %H:%M:%S', time.localtime(ctime)))
# print(os.path.getsize(path), 'байт')# размер
# print(os.path.getctime(path))# время создание
# print(os.path.getatime(path))# время последнего доступа
# print(os.path.getmtime(path))# время последнего изменения

# file_path = 'pop/12.txt'
# if os.path.exists(file_path):
#     dir0, name = os.path.split(file_path)
#     atime = os.path.getatime(file_path)
#     print(f'{name} ({dir0}) - время последненго доступа:,', atime, 'сек')
# else:
#     print(f'Файл {file_path } не существует')
#
# print(os.path.isfile(file_path))
# print(os.path.isdir(file_path))

# objs = os.listdir('nested')
# # print(objs)
# for o in objs:
#     p = os.path.join('nested',o)
#     # print(p)
#     if os.path.isfile(p):
#         print(f'{o} - file -{os.path.getsize(p)}, байт')
#     else:
#         print(f'{o} - dir')

# objs = os.listdir('nested')
# # print(objs)
# for o in objs:
#     p = os.path.join('nested',o)
#     print('1', p)
#     if os.path.isfile(f'{p}'):
#          os.remove(p)
#     else:
#         print(p)

import time
# def dell_1(tree_1):
#     print(f'Удадение файлов в папках {tree_1}')
#     print('-' * 50)
#     for root, dirs, files in os.walk(tree_1):
#         print('фыйл', files)
#         for d in dirs:
#             print('dirs', d)
#             for f in files:
#                 print('files', f)
#                 file_dell = os.path.join(root, d, f)
#                 print('1233', file_dell)
#                 if os.path.isfile(f'{file_dell}'):
#                     print('0>>>', file_dell)
#                     os.remove(file_dell)
#                     print(file_dell)
#                 else:
#                     print('1>>',file_dell)
#
#
#
#      # print('-' * 50)
# dell_1('Work')
