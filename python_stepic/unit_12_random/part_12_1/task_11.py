import random

n = int(input())    # количество попыток
result ={0:'Орел',
         1:'Решка'}
for i in range(n):
    print(result[random.randrange(len(result))])


from random import randint
a = {1 : 'Орел', 2 : 'Решка'}
for i in range(int(input())):
    print(a.get(randint(1, 2)))
