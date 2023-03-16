from random import*
from string import ascii_letters
string = ascii_letters

# print(*[string[randrange(len(string))] for _ in range(int(input()))], sep = '')
print(*[choice(string) for _ in range(int(input()))], sep = '')

for _ in range(int(input())):
    print(chr(choice([randint(65, 90), randint(97, 122)])), end='')
