# Задание-1: уравнение прямой вида y = kx - b задано ввиде строки.
# Определить координату y, точки с заданной координатой x

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y
k=float((equation[equation.find('=')+1:equation.find('x')]).strip())
if '+' in equation:
    b=float((equation[equation.find('+')+1:]).strip())
else:
    b=-float((equation[equation.rfind('-')+1:]).strip())

#print(k,b)
y=k*x+b

print('x,y:',x,y)
print('')
# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy', проверить корректно ли введена дата
# Условия коррекности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31) (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год приводиться к целому положитеьному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом (т.е. 2 - для дня, 2- месяц, 4 -год)


# Пример корректной даты
date = '01.11.1985'

def myRdata(dat):
    daymonth=(31,29,31,30,31,30,31,31,30,31,30,31)
    if len(dat[:dat.find('.')])==2 and len(dat[dat.find('.')+1:dat.rfind('.')])==2 and len(dat[dat.rfind('.')+1:])==4 and int(dat[dat.rfind('.')+1:])>=1 and int(dat[dat.rfind('.')+1:])<=9999 and int(dat[dat.find('.')+1:dat.rfind('.')])>=1 and int(dat[dat.find('.') + 1:dat.rfind('.')]) <= 12 and int(dat[:dat.find('.')])>=1 and int(dat[:dat.find('.')])<=daymonth[int(dat[dat.find('.') + 1:dat.rfind('.')])]:
        return 'Корректная дата'
    else:
        return 'Некорректная дата'

print(date, myRdata(date))
# Примеры некорректных дат
date = '01.22.1001'
print(date, myRdata(date))

date = '1.12.1001'
print(date, myRdata(date))

date = '-2.10.3001'
print(date, myRdata(date))

print('')
# Задание-3: "Перевернутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню — расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната, затем идет два этажа
# на каждом из которых по две комнаты, затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача: нужно научится по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3


def vavilon(N):
    i = 1
    n = 1  # номер последней комнаты в квадратном блоке
    while n <= N:
        i += 1
        n += i*i -1
    return 'квартира находится на '+str(sum(range(i+1))-1-(n-N)//i)+' этаже, '+str((N-n)%i+1)+'-я слева\n'

N=28
print(N, vavilon(N))

N=49
print(N, vavilon(N))

N=13
print(N, vavilon(N))

N=11
print(N, vavilon(N))

N=85
print(N, vavilon(N))

N=1974
print(N, vavilon(N))

N=15490
print(N, vavilon(N))

N=654159
print(N, vavilon(N))