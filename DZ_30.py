import json


class Map:
    # t1 = {}
    def __init__(self, dict_1):
        self.dict_1 = dict_1

    def __str__(self):
        return f'{self.dict_1}'

    def add_map(self, dict_new):
        self.dict_1.update(dict_new)

    def del_country(self, index):
        self.dict_1.pop(index)

    def data_search(self, key):
        print(self.dict_1[key])

    def data_editing(self, key, values):
        self.dict_1[key] = values
        return self.dict_1

    def show_dict(self):
        print(self.dict_1)

    def dump_to_json(self, file_map):
        data = self.dict_1
        with open(file_map, 'w+', encoding="UTF-8") as f:
            json.dump(data, f, ensure_ascii=False)

    def load_from_file(self, file_map):
        with open(file_map, 'r', encoding="UTF-8") as f:
            print(json.load(f))


t1 = Map({"Россия": "Москва"})
file_map = "map.json"

v = input(
    f"{'*' * 50}\nВыбор действий:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n4 - редактирование данных\n5 - просмотр данных\n6 - завершение работы\nВведите:")
if v == '1':
    v1 = {input("Введите название страны (с заглавной буквы:)"): input("Введите название столицы (с заглавной буквы)")}
    t1.add_map(v1)
    t1.dump_to_json(file_map)
    print(t1)
if v == '2':
    print(t1)
    t1.del_country(input("Введите страну"))
    print(t1)
if v == '3':
    t1.data_search(input("Введите страну"))
if v == '4':
    t1.data_editing(input("Введите страну"), input("Введите столицу"))
    print(t1)
if v == '5':
    t1.show_dict()
if v == '6':
    t1.dump_to_json(file_map)
    t1.load_from_file(file_map)
    print("Работа завершена")

