from copy import copy
from pprint import pprint 
import os

base_path = os.getcwd()
dir_name = 'homework_7'
file_name = 'recipes.txt'
fullpath = os.path.join(base_path, dir_name, file_name)

# словарь рецептов

with open(fullpath, 'r', encoding = "utf-8") as file:
    cook_book = {}

    for line in file:
        dish_name = line.strip()
        quantity = int(file.readline().strip())
        ingridients = []

        for i in range(quantity):
            work_dict = {}
            item = file.readline().strip()
            item = item.split('|')
            work_dict['ingredient_name'] = item[0]
            work_dict['quantity'] = int(item[1])
            work_dict['measure'] = item[2]
            ingridients.append(work_dict)
        cook_book[dish_name] = ingridients
        file.readline()
           
pprint(cook_book)

# Задача 2

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for item in dishes:
        value = cook_book[item]
        for el in value:
            if el['ingredient_name'] not in shop_list.keys():
                local_dict = {}
                local_dict['measure'] = el['measure']
                local_dict['quantity'] = el['quantity'] * person_count
                shop_list[el['ingredient_name']] = local_dict
            else:
                id = shop_list[el['ingredient_name']]  
                id['quantity'] += el['quantity'] * person_count                
    print(shop_list)
    return shop_list


def list_by_dishes():
    dishes = []
    while True:
        dish = input('Укажите название блюда: ').capitalize()
        if dish in cook_book.keys():
            dishes.append(dish)
            print(f'Вы добавили в список {dish}. Добавить еще блюдо в список? (да/нет)')
            command_ = input('да - добавить еще блюдо в список, нет - перейти к расчету ингридиентов: ').lower()
            if command_ == 'да':
                continue
            elif command_ == 'нет':
                person_count = int(input('Укажите количество персон: '))
            print(f'Итоговый список блюд: {", ".join(dishes)}; расчет на {person_count} персон')
            get_shop_list_by_dishes(dishes, person_count)
            break
        else:
            print(f'Указанного блюда нет в списке рецептов. Укажите блюдо из списка')
            continue
       
list_by_dishes()

# Задача 3

from glob import glob
from os.path import basename
import operator

dir_3 = 'case_3' # папка с файлами
path_3 = os.path.join(base_path, dir_name, dir_3)

list_path = list(glob(os.path.join(path_3, '*.txt'))) # список путей к файлам

result_file = os.path.join('C:\\TEST\\homework_7\\case_3', 'result_file') # итоговый файл
if not os.path.exists('C:\\TEST\\homework_7\\case_3'):
    os.makedirs('C:\\TEST\\homework_7\\case_3')

def directory_dict(list_path): # создаем структуру данных из папки и сортируем ее
    case_dict = {}
    for i in list_path:
        with open (i, 'r', encoding = "utf-8") as file_obj:
            file_obj_name = basename(file_obj.name)
            lines = file_obj.readlines()
            len_str = len(lines)
            list_for_key = [len_str]
            case_dict[file_obj_name] = list_for_key
            for j in lines:
                text_line = j.strip('\n')
                list_for_key.append(text_line)       
    sorted_tuple = sorted(case_dict.items(), key=operator.itemgetter(1))
    return sorted_tuple

def write_sorted(result_file):
    sorted_tuple = directory_dict(list_path)
    with open (result_file, 'a', encoding = "utf-8") as file_obj:
        for i in sorted_tuple:
            res = i[0] 
            file_obj.write(res)
            file_obj.write('\n')
            for el in i[1]:
                res = str(el)
                file_obj.write(res)
                file_obj.write('\n')
    return file_obj

write_sorted(result_file)         


