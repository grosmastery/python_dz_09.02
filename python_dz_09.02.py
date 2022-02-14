'''
1) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена самых молодых.
б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
в) Посчитать среднее количество лет всех людей из списка.
'''

from operator import itemgetter

users_list = [
    {"name": "John", "age": 15}, {"name": "Jackson", "age": 12},
    {"name": "Anna", "age": 54}, {"name": "Eveelin", "age": 18},
    {"name": "Alice", "age": 12}, {"name": "Jack", "age": 45}
    ]
users_list.sort(key = itemgetter('age'))
for dict_from_list in users_list:
    if dict_from_list == users_list[0]:
        for user_age in users_list:
            if user_age.get('age') == dict_from_list.get('age'):
                print(user_age.get('name'))

print('\r')

users_list.sort(key = lambda i: len(i['name']), reverse=True )
for dict_from_list in users_list:
    if dict_from_list == users_list[0]:
        for user_name in users_list:
            if len(user_name.get('name')) == len(dict_from_list.get('name')):
                print(user_name.get('name'))

print('\r')

average_age = 0
for idx, user_age in  enumerate(users_list):
    average_age += user_age.get('age')
    if idx == len(users_list) - 1:
        average_age /= (idx + 1)
print(average_age)

print('\r') #############################################

'''
2. Написать функцию которой передается два параметра - две строки.
Функция возвращает список в который поместить те символы,
которые есть в обеих строках хотя бы раз.
'''

my_list = []
def average_elements(string1, string2):
    for str_element1 in set(string1):
        if str_element1 == ' ':
            continue
        for str_element2 in set(string2):
            if str_element2 == str_element1:
                my_list.append(str_element2)
                break
    return my_list
print(average_elements('1 2 3 4 5 gfdg 1 yrre', '2 1 3 s gret 4 5 cbc 3 1'))

print('\r') ################################################

'''
3. Написать функцию которой передается два параметра - две строки.
Функция возвращает список в который поместить те символы, которые есть в обеих строках,
но в каждой только по одному разу.
'''

my_list3 = []
def func_elements(string1, string2):
    dict_str1 = {}
    str_list1 = []
    for str1 in string1:
        if str1 not in dict_str1.keys():
            dict_str1[str1] = 1
        else:
            dict_str1[str1] += 1
    for value1, key1 in dict_str1.items():
        if key1 == 1 and value1 != ' ':
            str_list1.append(value1)

    dict_str2 = {}
    str_list2 = []
    for str2 in string2:
        if str2 not in dict_str2.keys():
            dict_str2[str2] = 1
        else:
            dict_str2[str2] += 1
    for value2, key2 in dict_str2.items():
        if key2 == 1 and value2 != ' ':
            str_list2.append(value2)


    for str_element1 in str_list1:
        for str_element2 in str_list2:
            if str_element2 == str_element1:
                my_list3.append(str_element1)
    return my_list3
print(func_elements('1 2 3 4 5 gfdg 1 yrre', '2 1 3 s gret 4 5 cbc 3 1'))

print('\r') ###########################################

'''
4. Даны списки names и domains (создать самостоятельно).
Написать функцию для генерирования e-mail в формате:
фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
Строку и число генерировать случайным образом.
'''

from random import randint, choice
import string

names = ['KingCrimson', 'StoneOcean', 'StarPlatinum', 'ZaWarudo']
domains = ['net', 'com', 'ua', 'ag', 'tv']
def create_email(func_names, func_domains):
    long_str = randint(1, 3)
    if long_str == 1:
        long_str = 5
    elif long_str == 2:
        long_str = 6
    elif long_str == 3:
        long_str = 7
    rand_int_to_str = str(randint(100, 999))
    rand_str = ''.join(choice(string.ascii_lowercase) for _ in range(long_str))
    rand_name = randint(0, len(names)-1)
    rand_domain = randint(0, len(domains)-1)
    create = names[rand_name] + '.' + rand_int_to_str + '@' + rand_str + '.' + domains[rand_domain]
    return create

e_mail = create_email(names, domains)
print(e_mail)
