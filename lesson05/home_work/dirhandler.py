#! python3 ;
# -*- coding: utf-8 -*-
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import re
import sys
import shutil
def create_dirs(number_dirs):
    try:
        for i in range(1,number_dirs+1):
            os.mkdir('dir_'+str(i))
        print(f'created {i} directories')
    except FileExistsError:
        print(f'Возможно файл c номером {i} существует, просьба проверить дирректорию {os.getcwd()}')
def delete_dirs(from_dir, to):
    try:
        for i in range(from_dir, to+1):
            os.rmdir('dir_'+str(i))
        print(f'dirs {from_dir}-{to} were deleted')
    except FileNotFoundError:
        print(f'Файла {i} не существует')
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def check_listdir(path=os.getcwd()):
    regex_only_dir = re.compile(r'\w+\.\w{2}')
    # listdir возвращает все содержипое папки, так что придется истить от файлов
    listdir=os.listdir(path)
    str_list_dir= " ".join(str(x) for x in listdir)
    files = regex_only_dir.findall(str_list_dir)
    dirs = [x for x in listdir if x not in files]
    print(dirs)
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def copy_current_file(path=sys.argv[0]):
    shutil.copy(path, path + '.copy')
    return True
##########################################################
################FOR NORMAL TASK###########################
##########################################################
def create_dir():
	dir = input('Введите название папки: ')
	try:
		os.mkdir(dir)
		print(f'Directory {dir} created successfully')
	except FileExistsError:
		print(f'Error creating dir {dir}, file exists')
def delete_dir():
	dir = input('Введите название папки: ')
	try:
		os.rmdir(dir)
		print(f'dir {dir} deleted')
	except FileNotFoundError:
		print(f'dir {dir} does not exist')
def change_dir():
    dir = input('Введите название папки, куда необходимо перейти: ')
    try:
        os.chdir(dir)
        print(f'dir changed to {os.getcwd()}')
    except FileNotFoundError:
        print(f'dir {dir} dosen`t exists')
def check_dir(path=os.getcwd()):
    listdir=os.listdir(path)
    print(listdir)
if __name__ == '__main__':
    create_dirs(11)
    delete_dirs(1,11)
    print(check_listdir())
    copy_current_file()

