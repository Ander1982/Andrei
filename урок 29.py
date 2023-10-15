import json


# date = {
#     "name": "Olga",
#     "age": 34,
#     "Hobby": ("ran", "Swem"),
#     True: 1,
#     20: None,
#     'children': [
#         {
#             "name": "NU",
#             "age": 6,
#         },
#     ]
# }
#
# print(date, end="\n\n")
# with open("data_file.json", "w") as fh:
#     json.dump(date, fh, indent=4)
#
# with open("data_file.json", "r") as fh:
#     file = json.load(fh)
# print(file)

# json_str = json.dumps(date)
# st = json.loads(json_str)
# print(st)

# x = {
#     "name": "Виктор"
# }
# y = json.dumps(x)
# print(json.loads(y))
# print(json.dumps(x))
# print(json.dumps(x, ensure_ascii=False))

# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8']
#
#     while len(name) != 7:
#         name += choice(letters)
#     # print(name)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#     return person
#
#
# def write_json(person_dict):
#     try:
#         data = json.load(open('persons.json'))
#     except FileNotFoundError:
#         data = []
#
#     data.append(person_dict)
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(gen_person())

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        # a = ""
        # for i in self.marks:
        #     a += str(i) + ", "
        # return f'Студент:{self.name} - {a[:-2]}'

        # a = ", ".join(map(str, self.marks))
        # return f"Студент:{self.name} - {a}"

        return f"Студент:{self.name} - {', '.join(map(str, self.marks))}"

    def add_mark(self, mark):
        self.marks.append(mark)

    def delete_mark(self, index):
        self.marks.pop(index)

    def edit_mark(self, index, new_marks):
        self.marks[index] = new_marks

    def average_marks(self):
        return round(sum(self.marks) / len(self.marks), 2)

    def dump_to_json(self, filename):
        data = {"name": self.name, "marks": self.marks}
        with open(filename, 'w') as f:
            json.dump(data, f)

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            print(json.load(f))


class Group:
    def __init__(self, students, group):
        self.students = students
        self.group = group

    def __str__(self):
        # a = ""
        # for i in self.students:
        #     a += str(i) + '\n'
        # return f"{a}"
        a = '\n'.join(map(str, self.students))
        return f"Группа: {self.group}\n{a}"

    @staticmethod
    def chandge_group(group1, group2, index):
        return group2.add_student(group1.remove_student(index))


    @staticmethod
    def dump_group(file, group):
        try:
            data = json.load(open(file))
        except FileNotFoundError:
            data = []

        with open(file, 'w') as f:
            stud_list = []
            for i in group.students:
                stud_list.append([i.name, i.marks])

            data.append(stud_list)
            json.dump(data, f, indent=2)

    @staticmethod
    def uploat_group(file):
        with open(file, 'r') as f:
            print(json.load(f))



    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, index):
        return self.students.pop(index)


st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
file1 = "student.json"
st1.dump_to_json(file1)
st1.load_from_file(file1)

print(st1)
# st1.add_mark(4)
# print(st1)
st1.delete_mark(2)
print(st1)
# st1.edit_mark(4, 5)
# print(st1)
# print(st1.average_marks())
# st2 = Student("Nikolaenko", [2, 3, 5, 4, 2])
# st3 = Student("Birukov", [2, 3, 5, 4, 2])
# sts = [st1, st2]
# my_group = Group(sts, "ГК Python")
# # # print(my_group)
# # # print()
# # my_group.add_student(st3)
# # # print(my_group)
# # print()
# # my_group.remove_student(1)
# # print(my_group)
# group22 = [st2]
# # print()
# my_group2 = Group(group22, "ГК Web")
# # print(my_group2)
# # Group.chandge_group(my_group, my_group2, 0)
# # print("-" * 50)
# # print(my_group)
# # print()
# # print(my_group2)
# file2 = 'group.json'
# # Group.dump_group(file2, my_group)
# # Group.dump_group(file2, my_group2)
# Group.uploat_group(file2)