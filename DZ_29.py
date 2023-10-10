from random import choice
import json


def gen_person():
    name = ''
    tel = ''
    key = ''

    key_list = ['1', '2', '3', '4', '5', '6', '7', '8']
    letters = ['a', 'b', 'c', 'd', 'e']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8']

    while len(name) != 7:
        name += choice(letters)
    # print(name)

    while len(tel) != 10:
        tel += choice(nums)

    while len(key) != 10:
        key += choice(key_list)

    person = {
        key: {
            'name': name,
            'tel': tel
        }
    }
    return person


def write_json(person_dict):
    try:
        data = json.load(open('3.json'))
    except FileNotFoundError:
        data = {}

    data.update(person_dict)
    with open('3.json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person())
