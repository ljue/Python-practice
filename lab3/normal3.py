import math

# Задание-1:
# Напишите функцию возвращающую ряд Фибоначчи с n-элемента до m-элемент
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n):
    if n > 2:
        return fibonacci(n-2) + fibonacci(n-1)
    else:
        return 1


def listFibonacci(n, m):
    l = []
    for i in range(n, m, 1):
        l.append(fibonacci(i))
    return l

print(listFibonacci(1,16),'\n')


# Задача-2:
# Напишите функцию сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную фукцию и метод sort()

def sort_to_max(origin_list):
    for i in range(len(origin_list)-1):
        for j in range(len(origin_list)-1, i, -1):
            if origin_list[j] < origin_list[j-1]:
                origin_list[j], origin_list[j-1] = origin_list[j-1], origin_list[j]
    return origin_list


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]), '\n')

# Задача-3:
# Напишите собственную реализацию функции filter
# Разумеется, внутри нельзя использовать саму функцию filter


def filter_func(func, spisok):
    a = []
    for i in spisok:
        if func(i):  # !=None:
            a.append(i)
    return a


def testfunc(x):
    if x > 5:
        return True

print(filter_func(testfunc, [2, 10, -10, 8, 2, 0, 14]), '\n')  # как сделать так чтоб работало и для лямбд - не знаю =(


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма


A1 = (1, 1)
A2 = (3, 3)
A3 = (5, 1)
A4 = (7, 3)
a = list(zip(A1, A2, A3, A4))
print(a)
# print(list(zip(A1,A2)))
# print(math.sqrt((a[0][1]-a[0][0])**2+(a[1][1]-a[1][0])**2))


def paral(a1, a2, a3, a4):
    a = list(zip(a1, a2, a3, a4))
    k = 0
    if math.sqrt((a[0][1]-a[0][0])**2+(a[1][1]-a[1][0])**2) == math.sqrt((a[0][3]-a[0][2])**2+(a[1][3]-a[1][2])**2):
        k += 1
    if math.sqrt((a[0][2]-a[0][0])**2+(a[1][2]-a[1][0])**2) == math.sqrt((a[0][3]-a[0][1])**2+(a[1][3]-a[1][1])**2):
        k += 1
    if math.sqrt((a[0][3] - a[0][0]) ** 2 + (a[1][3] - a[1][0]) ** 2) == math.sqrt((a[0][2] - a[0][1]) ** 2 + (a[1][2] - a[1][1]) ** 2):
        k += 1
    if k >= 2: return True
    else: return False

print(paral(A1, A2, A3, A4))