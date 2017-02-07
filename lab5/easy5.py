import sys
import os
from os.path import isfile

import shutil

# Задача-1:
# Напишите скрипт создающий директории dir_1 - dir_9 в папке из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def create_dir(name_dir,my_path):
    dir_path = os.path.join(my_path, name_dir)
    try:
        os.mkdir(dir_path)
        print('Успешно создано')
    except FileExistsError:
        print('Невозможно создать')


def delete_dir(name_dir,my_path):
    dir_path = os.path.join(my_path, name_dir)
    try:
        os.rmdir(dir_path, dir_fd=None)
        print('Успешно удалено')
    except FileNotFoundError:
        print('Невозможно удалить')

my_path=os.getcwd()
if __name__=='__main__':
    for i in range(9):
        name1='dir_'+str(i+1)
        create_dir(name1,my_path)
if __name__=='__main__':
    for i in range(9):
        name1 = 'dir_' + str(i+1)
        delete_dir(name1,my_path)

    # Задача-2:
# Напишите скрипт отображающий папки текущей директории
if __name__=='__main__':
    list_my=os.listdir(os.getcwd())
    list_dir=[]
    for i in list_my:
        if not isfile(os.path.join(os.getcwd(), i)):
            list_dir.append(i)
    print(list_dir)


# Задача-3:
# Напишите скрипт создающий копию файла, из которого запущен данный скрипт
if __name__=='__main__':
    dir_path1 = os.path.join(os.getcwd(), 'easy5.py')
    print(dir_path1)
    dir_path2 = os.path.join(os.getcwd(), 'newEasy')
    shutil.copyfile(dir_path1, dir_path2)


def change_dir(name_dir,my_path):
    my_path1=my_path
    try:
        my_path = my_path +'\\'+ name_dir
        my_list = os.listdir(my_path)
        print('Успешно перешел')
        return my_path
    except:
        print('Невозможно перейти')
        return my_path1

def rechange_dir(my_path):
    my_path1 = my_path
    try:
        my_path = my_path[:my_path.rfind('\\')]
        my_list = os.listdir(my_path)
        print('Успешно перешел')
        return my_path
    except:
        print('Невозможно перейти')
        return my_path1