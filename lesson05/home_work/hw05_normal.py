#! python3 ;
# -*- coding: utf-8 -*-
import dirhandler
# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"
choice_to_function = {
    1: dirhandler.change_dir,
    2: dirhandler.check_dir,
    3: dirhandler.delete_dir,
    4: dirhandler.create_dir
}
def print_user_message():
    print("С помощью этой программы вы можете:")
    print('''
      1. Перейти в папку
      2. Просмотреть содержимое текущей папки
      3. Удалить папку
      4. Создать папку
    Выберите нужный пункт:
    ''')
# def directory_func():
###try1
# def dict_funct():
#     users_choice = int(input())
#     if users_choice == 1:
#         dirhandler.change_dir()
#     elif users_choice == 2:
#         dirhandler.check_listdir()
#     elif users_choice == 3:
#         dirhandler.delete_dir()
#     elif users_choice == 4:
#         dirhandler.create_dir()
# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
#try2
if __name__ == '__main__':
    try:
        print_user_message()
        users_choice=int(input())
        if choice_to_function.get(users_choice):
            choice_to_function[users_choice]()
        else:
            print("Задан неверный пункт")
    except:
        print('Ничего не введено')