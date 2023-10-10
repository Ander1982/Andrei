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

with open("texts1.csv") as r_file:
    file_reader = csv.reader(r_file, delimiter=";")
    count = 0
    for row in file_reader:
        if count == 0:
            print(f"Файл содержит столбцы: {', '.join(row)}")
        else:
            print(f"\t{row[0]} - {row[1]}")
        count += 1
    print(f"Всего в файле {count} строк.")