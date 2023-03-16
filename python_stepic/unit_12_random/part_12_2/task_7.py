# Почтовый индекс в Латверии имеет вид: LetterLetterNumber_NumberLetterLetter, где Letter – заглавная буква английского алфавита, Number – число от 00 до 9999 (включительно).

# Напишите функцию generate_index(), которая с помощью модуля random генерирует и возвращает случайный корректный почтовый индекс Латверии.

# Примечание 1. Пример правильного (неправильного) индекса Латверии:

# AB23_56VG          # правильный
# V3F_231GT          # неправильный
# Примечание 2. Обратите внимание на символ _ в почтовом индексе.

# Примечание 3. Вызывать функцию generate_index() не нужно, требуется только реализовать.



from string import ascii_uppercase as a_u
from random import randrange as r
from random import choice


def generate_index():
    return f'{choice(a_u)}{choice(a_u)}{r(100)}_{r(100)}{choice(a_u)}{choice(a_u)}'

print(generate_index())
