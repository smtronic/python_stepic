# Сумма дробей 2
# На вход программе подается натуральное число n.
# Напишите программу, которая вычисляет и выводит рациональное число, равное значению выражения
# Формат входных данных
# На вход программе подается натуральное число n.

# Формат выходных данных
# Программа должна вывести ответ на задачу.

# Примечание 1. Результирующая дробь должна быть несократимой.

# Примечание 2. Для вычисления факториала можно использовать функцию factorial из модуля math.

from fractions import Fraction as F
from math import factorial
x = int(input())
res = set()
result = [res.add(F(1, factorial(i))) for i in range(1, x + 1)]
print(sum(res))
