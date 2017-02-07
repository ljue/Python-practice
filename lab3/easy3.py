# Задание-1:
# Напишите функцию округлящую полученное произвольное десятичное число,
# до кол-ва знаков (кол-во знаков передается вторым аргументом)
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные и функции и функции из модуля math


def my_round(number, ndigits):
    if len(str(number).split('.')[1])>ndigits:
        if int(str(number).split('.')[1][ndigits])<5:
            return number-number%(10**(-ndigits))
        else:
            return number-number%(10**(-ndigits))+10**(-ndigits)

#    pass
print(my_round(2.1234567, 5),'\n')

# Задание-2:
# Дан шестизначный номер билета, определить является ли билет счасливым
# Решение реализовать в виде функции
# Билет считается счастливым, если сумма его первых и последних цифр равны
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    return (ticket_number%1000)//100+(ticket_number%100)//10+ticket_number%10==(ticket_number//1000)%10+(ticket_number//10000)%10+ticket_number//100000

print(lucky_ticket(123321))
print(lucky_ticket(173245))
print(lucky_ticket(284564))
#pass