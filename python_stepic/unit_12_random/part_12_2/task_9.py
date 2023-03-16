# Напишите программу, которая с помощью модуля random генерирует
# 100 случайных номеров лотерейных билетов и выводит их каждый на отдельной строке.
# Обратите внимание, вы должны придерживаться следующих условий:

# номер не может начинаться с нулей;
# номер лотерейного билета должен состоять из 77 цифр;
# все 100100 лотерейных билетов должны быть различными.

from random import randint

def lucky_list(n=int):
    lucky_list = []
    while len(lucky_list) < n :
        number = randint(999999, 9999999)
        if number not in lucky_list:
            lucky_list.append(number)
    return lucky_list
n = 100

for num in lucky_list(n):
    print(num)
