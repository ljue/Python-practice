#!/usr/bin/python3

"""Лото

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random


def digit(li):
    d = random.randrange(1, 90)
    if d in li:
        return digit(li)
    else:
        li.append(d)
        return d


def stroka(li1=[]):
    li = [digit(li1) for _ in range(5)]
    li.sort()
    for i in range(4):
        li.insert(random.randrange(1, 9), ' ')
    return li


class Gender:
    PERSON = 0
    COMPUTER = 1


class Card(Gender):
    def __init__(self,gen):
        l1=stroka()
        l=[i for i in l1]
        l2=stroka(l)
        l3=stroka(l)
        self.card=l1+l2+l3
        self.gen=gen
        self.count_tire=0


    def tire(self,dig,znak=''):
        if self.gen==Gender.PERSON:
            if znak=='y':
                if dig in self.card:
                    n=self.card.index(dig)
                    self.card.remove(dig)
                    self.card.insert(n,'-')
                    self.count_tire+=1
                    return True
                else: return False
            else:
                if dig in self.card:
                    return False
                else: return True
        else:
            if dig in self.card:
                n = self.card.index(dig)
                self.card.remove(dig)
                self.card.insert(n, '-')
                self.count_tire += 1




    def __len__(self):
        return len(self.card)

    def __str__(self):
        if self.gen==Gender.COMPUTER:
            sum='-- Карточка компьютера ---\n'
        elif self.gen==Gender.PERSON:
            sum = '------ Ваша карточка -----\n'
        else: sum = '--------------------------\n'
        for index,x in enumerate(self.card):
            if (index+1)%9:
                sum += '{:<3}'.format(str(x))
            else:
                sum += '{:<3}'.format(str(x)) + '\n'
        sum+='--------------------------\n'
        return sum

class GameLoto:
    def __init__(self):
        self.user=Card(Gender.PERSON)
        self.pk=Card(Gender.COMPUTER)
        self.li=[]
        self.game_on=True

    @property
    def game_On(self):
        return self.game_on

    def hod(self):
        print(self.user)
        print(self.pk)
        dig=digit(self.li)
        print('Новый бочонок: {} (осталось {})'.format(dig,90-len(self.li)))
        self.pk.tire(dig) #  выход из игры если комп выиграл
        if self.pk.count_tire < 15:
            while(True):
                n=input('Зачеркнуть цифру? (y/n) ')
                if n=='y' or n=='n':
                    break
                else:
                    continue
            if self.user.tire(dig,n):
                if self.user.count_tire==15:
                    print('YOU WIN')
                    print('GAME OVER')
                    self.game_on = False
            else:
                print('YOU LOSE')
                print('GAME OVER')
                self.game_on=False
        else:
            print('YOU LOSE')
            print('GAME OVER')
            self.game_on = False


game1=GameLoto()
while(game1.game_On==True):
    game1.hod()