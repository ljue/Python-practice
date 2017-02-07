# Задание-1:
# Написать программу выполняющую операции(сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (все выражение вводится целиком в виде строки)
# Вывод: 1 17/42 (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 2/3


'''
1 - Сделано для "идеального случая" Нет времени переделывать :(

Не будет работать для
-2/3 - -2

'''




y='5/6 + 4/7'

def sum(x,znak):
    '''
    Считает сумму дробей. Результат - простая дробь.
    :param x:
    :param znak:
    :return:
    '''
    sx0=simpleDig(x.split(znak)[0].strip())
    sx1 = simpleDig(x.split(znak)[1].strip())
    sx00=sx0.split('/')[0]
    sx01 = sx0.split('/')[1]
    sx10 = sx1.split('/')[0]
    sx11 = sx1.split('/')[1]
    znamenatel=int(nok(int(sx01),int(sx11)))
    chislitel1=int(sx00)*znamenatel/(int(sx01))
    chislitel2=int(sx10)*znamenatel/(int(sx11))
    if znak=='-':
        chislitel2=-chislitel2
    chislitel=int(chislitel2+chislitel1)
    return str(chislitel)+'/'+str(znamenatel)

def simpleDig(a1):
    '''
    переводит сложные дроби в простые
    :param a1:
    :return:
    '''
    if ' ' in a1:
        a10=a1.split(' ')[0]
        a11=a1.split(' ')[1]
        a110=a11.split('/')[0]
        a111 = a11.split('/')[1]
        return str(int(a10)*int(a111)+int(a110))+'/'+a111
    else: return a1

def bigDig(res):
    '''
    Переводит простую дробь в сложную
    :param res:
    :return:
    '''
    a0 = res.split('/')[0]
    a1 = res.split('/')[1]
    ares = int(a0)//int(a1)
    if ares>0:
        return str(ares)+' '+str(int(a0)%int(a1))+'/'+a1
    else: return res

def nok(n, m):
    return (n / nod(n, m)) * m

def nod(a, b):
    while b:
        a, b = b, a % b
    return a

def calc(y):
    if '+' in y:
        znak='+'
    if '-' in y:
        znak='-'
    simplesum=sum(y, znak)
    return bigDig(simplesum)

print(calc(y),'\n')



# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработаю норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП пропорциональную норме.
# Кол-во часов, которые были отработаны указаны в файле "data/hours_of"

import os


path = os.path.join('data', 'hours_of.txt')
fhours = open(path, 'r', encoding='UTF-8')

path = os.path.join('data', 'hoursWorkers.txt')
fhw = open(path, 'w', encoding='UTF-8')
fhw.write('{:<20}'.format('Имя')+'{:<20}'.format('Фамилия')+'{:<20}'.format('Зарплата')+'\n')

for hline in fhours:
    k=0
    h=hline.split('\n')[0].split(' ')
    while h.count('')>0:
        h.remove('')
    if h[0] != '\ufeffИмя':
        k+=1
        path = os.path.join('data', 'workers.txt')
        fworkers = open(path, 'r', encoding='UTF-8')
        for wline in fworkers:
            w = wline.split('\n')[0].split(' ')
            while w.count('') > 0:
                w.remove('')
            if w[0] != '\ufeffИмя':
                k+=1
                if h[0]==w[0] and h[1]==w[1]:
                    hw='{:<20}'.format(h[0])+'{:<20}'.format(h[1])
                    if int(h[2])<=int(w[4]):
                        hw+='{:<20}'.format( str( int( int(h[2]) /int(w[4]) *int(w[2]) ) ))+'\n'
                    else:
                        hw += '{:<20}'.format( str( int( int(w[2]) + ( int(h[2]) - int(w[4]) ) / int(w[4]) *2* int(w[2]) ) ))+'\n'
        fworkers.close()
    if k>=2:
        print(hw)
        fhw.write(hw)

fhours.close()
fhw.close()

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов
# Записать в новые файлы все фрукты начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание что нет фруктов начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

Alf=list(map(chr, range(ord('А'), ord('Я')+1)))
#print(Alf)


path = os.path.join('data', 'fruits.txt')
f = open(path, 'r', encoding='UTF-8')
for line in f:
    for A in Alf:
        if A in line:
            str1="data\\newfruits\\fruits_"+A+".txt"
            newF=open(str1,'a', encoding='UTF-8')
            newF.write(line)
            newF.close()
f.close()
