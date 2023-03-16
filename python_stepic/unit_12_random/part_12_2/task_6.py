# IP адрес состоит из четырех чисел из диапазона от 00 до 255255 (включительно) разделенных точкой.

# Напишите функцию generate_ip(), которая с помощью модуля random  генерирует и возвращает случайный корректный IP адрес.

# Примечание 1. Пример правильного (неправильного) IP адреса:

# 192.168.5.250        # правильный
# 199.300.521.255      # неправильный


def generate_ip():
    from random import randrange
    return f'{randrange(256)}.{randrange(255)}.{randrange(10)}.{randrange(255)}'
