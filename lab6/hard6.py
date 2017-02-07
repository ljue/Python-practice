# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчеты заработной платы (файл "data/workers"). Рассчитайте зарплату всех работников,
# зная что они получат полный оклад, если отработаю норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают удвоенную ЗП
# пропорциональную норме.
# Кол-во часов, которые были отработаны указаны в файле "data/hours_of"

# С использованием классов.
# Рализуйте классы сотрудников так, чтобы на вход функции-конструктора каждый работник получал строку из файла

import os


class People:
    def __init__(self,fam,im):
        self.fam=fam
        self.im=im

    def __str__(self):
        return self.fam + ' ' + self.im



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