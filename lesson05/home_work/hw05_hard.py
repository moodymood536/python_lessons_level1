#! python3;
# -*- coding: utf-8 -*-
# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.
# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")
    print("rm <file_name> - удаляет указанный файл")

def rm():
    if not dir_name:
        print("Необходимо указать имя удаляемого файла")
        return False
    else:
        permission = input('Точно удаляем? y/n: ').lower()
        if not permission or permission == 'no' or permission != 'y':
            print('NO')
            return False
        else:
            if os.path.isabs(dir_name):
                dir_path = dir_name
                print('abs path')
            else:
                dir_path = os.path.join(os.getcwd(), dir_name)
                print('not_abs path')
            try:
                os.remove(dir_path)
                print(f'Файл {dir_path} удален')
            except FileNotFoundError:
                print(f'Файл {dir_name} не существует')
def ls():
    print(os.getcwd())

def cd():
    if not dir_name:
        print("Необходимо указать имя директории, куда переходим")
        return False
    else:
        prev_dir = os.getcwd()
        if os.path.isabs(dir_name):
            dir_path = dir_name
            print('abs path')
        else:
            dir_path = os.path.join(os.getcwd(), dir_name)
            print('not_abs path')
        try:
            os.chdir(dir_path)
            print(f'Рабочая дирректория изменилась с {prev_dir} \nна {os.getcwd()}')
        except FileNotFoundError:
            print(f'Директория {dir_name} не существует')

def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    if os.path.isabs(dir_name):
        dir_path = dir_name
        print('abs path')
    else:
        dir_path = os.path.join(os.getcwd(), dir_name)
        print('not_abs path')
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))
def cp():
    # В данной функции под dir_name понимаем путь до файла
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    if os.path.isabs(dir_name):
        file_path = dir_name
        print('abs path')
    else:
        file_path = os.path.join(os.getcwd(), dir_name)
        print('not_abs path')
    print(file_path)
    shutil.copy(file_path, file_path + '.copy')
    print('Копия файла создана')

def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": cp,
    "cd": cd,
    "ls": ls,
    "rm": rm
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
