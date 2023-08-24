f = open('DZ_18.txt', 'w')
f.write('1.Замена строки в текстовом файле; \n2.изменить строку в списке;\n3.записать список в файл')
f.close()

f = open('DZ_18.txt', 'r')
read_file = f.readlines()
print(read_file)
a = (int(input('Введите номер стоки, которую желаете удалить(1-3)>>:' ))-1)
read_file[a] = ''
print(read_file)
f.close()

f = open('DZ_18.txt', 'w')
f.writelines(read_file)
f.close()
