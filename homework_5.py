"""
Третье домашнее задание
Цель из файлов json и csv выбрать необходимые данные и предать их в новый json
Дата 09.04.2022
"""
import copy
import json
from csv import DictReader

# локальные переменные
new_data = []
new_dict = {}
csv_list = []

# читаем данные из json и сохраняем в users
with open("files/users.json", 'r') as file_json:
    users = json.load(file_json)

# читаем данные из csv и сохраняем в csv_list
with open("files/books.csv", newline='') as file_csv:
    reader = DictReader(file_csv)
    for row in reader:
        csv_list.append(row)

# пройти по каждому юзеру из json и взять необходимые данные (name, gender, address, age) и добавить в словарь new_dict
for ch in range(len(users)):
    new_dict['name'] = users[ch]['name']
    new_dict['gender'] = users[ch]['gender']
    new_dict['address'] = users[ch]['address']
    new_dict['age'] = users[ch]['age']

    # добавляем новый список books в словарь new_dict к юзеру для обогащения книгами
    new_dict['books'] = []

    # пройти по всем книгам с шагом len(users) и добавить книги к юзеру
    for count in range(ch, len(csv_list), len(users)):
        new_dict['books'].append(csv_list[count])

    # скопировать словарь в transmitted_dictionary (для того что бы данные в словаре при следующем цикле
    # не перезатерлись)
    transmitted_dictionary = copy.deepcopy(new_dict)

    # добавить созданный словарь в список new_data из которого будем делать json
    new_data.append(transmitted_dictionary)

# создать json из new_data
with open("files/result.json", 'w') as write_json:
    json.dump(new_data, write_json, indent=4)
