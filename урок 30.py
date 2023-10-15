# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# # print(response)
# todos = json.loads(response.text)
# todos_by_users = {}
# for todo in todos:
#     if todo["completed"]:
#         try:
#             todos_by_users[todo["userId"]] += 1
#         except KeyError:
#             todos_by_users[todo["userId"]] = 1
#
# print(todos_by_users)
#
# top_users = sorted(todos_by_users.items(), key=lambda x: x[1], reverse=True)
# print(top_users)
# max_complete = top_users[0][1]
# print(max_complete)
# users = []
# for user, num_complete in top_users:
#     if num_complete < max_complete:
#         break
#     users.append(user)
#
# print(users)
# m_users = " and ".join(map(str, users))
# print(m_users)
# m = 'Users' if len(users) > 1 else "User"
# print(f"{m} {m_users} completed {max_complete} TODOs")
#
# print(users)
# def keep(todo):
#     is_complete = todo['completed']
#     # print(is_complete)
#     has_max_count = (todo['userId']) in users
#     # print(has_max_count)
#     return is_complete and has_max_count
#
#
# with open("data8.json", "w") as f:
#     filter_todos = list(filter(keep, todos))
#     # print(filter_file)
#     json.dump(filter_todos, f, indent=2)
import csv

# with open("texts1.csv") as r_file:
#     file_reader = csv.reader(r_file, delimiter=";")
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         else:
#             print(f"\t{row[0]} - {row[1]}")
#         count += 1
#     print(f"Всего в файле {count} строк.")

# with open("texts1.csv") as r_file:
#     file_name = ['имя', 'Профессия', 'Год рождения']
#     file_reader = csv.DictReader(r_file, delimiter=";", fieldnames=file_name)
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файлы содержите столбцы: {', '.join(row)}")
#         print(f"{row}")

# with open('student.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=";")
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(["Женя", 9, 15])
#     writer.writerow(["Саша", 5, 11])
#     writer.writerow(["Маша", 3, 10])
#
#
# ata = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']
#
# with open('sw.cvs', 'w') as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     for row in data:
#         writer.writerow(data)
#
#     writer.writerows(data)

# with open('student_1.csv', "w") as f:
#     names = ['имя', 'Возраст']
#     file_write = csv.DictReader(f, delimiter=";", lineterminator="\r", fieldnames=names)
#     file_write.writerow({'Имя': 'Вова', "Возраст": 14})
#     file_write.writerow({'Имя': 'Вася', "Возраст": 12})
#     file_write.writerow({'Имя': 'Вика', "Возраст": 10})


# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open("dict.csv", "w") as f:
#     writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=list(data[0].keys()))
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)

# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
#
# with open("todos.csv", "w") as f:
#     writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=list(todos[0].keys()))
#     writer.writeheader()
#     for d in todos:
#         writer.writerow(d)

