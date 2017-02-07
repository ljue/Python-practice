# Все задачи текущего блока решите с помощью генераторов!

# Задание-1:
# Дан список, заполненный произвольными целыми цифрами, получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

list1 = [1, 2, 4, 0]
list2 = [x**2 for x in list1]
print(list1,'-->',list2)

# Задание-2:
# Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.

list1 = ['яблоко', 'апельсин', 'манго', 'банан', 'гранат']
list2 = ['гранат', 'мандарин', 'ананас', 'груша', 'манго', 'банан']
list3 = [x for x in list1 if x in list2]
print(list3)
# Задание-3:
# Дан список, заполненный произвольными числами. Получить список из элементов исходного, удовлетворяющих след. условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

list1 = [3, 4, 0, -3, 12, 18]
list2 = [x for x in list1 if x%3 == 0 and x > 0 and x%4 != 0]
print(list2)