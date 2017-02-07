from lab5.easy5 import create_dir
from lab5.easy5 import delete_dir
from lab5.easy5 import change_dir
from lab5.easy5 import rechange_dir
import sys
import os

# Задача-1:
# Напишите небольшую консольную утилиту, позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов: 1, 3,4, программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел", "Невозможно создать/удалить/прейти"

# Для решения данной задачи используйте алоритмы из задания easy,
# оформленныйе в виде соответствующих функций, и импортированные в данный файл из easy.py


def menu():
    print('1. Перейти в папку\n2. Просмотреть содержимое текущей папки\n3. Удалить папку\n4. Создать папку\n'\
          '5. Перейти выше по каталогу\n0. Выход')

my_path=os.getcwd()

menu()
while(True):
    try:
        n = int(input())
    except:
        print('Введите номер выбранного пункта меню')
    if n==0:
        sys.exit()
    if n==4:
        newstr=input('Введите имя новой папки ')
        create_dir(newstr,my_path)
    if n==3:
        newstr = input('Введите имя папки, которую нужно удалить ')
        delete_dir(newstr,my_path)
    if n==2:
        my_list = os.listdir(my_path)
        print(my_list)
    if n==1:
        newstr = input('Введите имя папки, в которую хотите перейти ')
        my_path = change_dir(newstr,my_path)
    if n==5:
        my_path = rechange_dir(my_path)
    print()