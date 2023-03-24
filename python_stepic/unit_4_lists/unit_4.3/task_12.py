# Упаковка дубликатов 🌶️
# На вход программе подается строка текста, содержащая символы. Напишите программу, которая упаковывает последовательности одинаковых символов заданной строки в подсписки.

# Формат входных данных
# На вход программе подается строка текста, содержащая символы, отделенные символом пробела.

# Формат выходных данных
# Программа должна вывести указанный вложенный список.

my_list = []

for c in input().split():
    if my_list and c in my_list[-1]:
        my_list[-1].append(c)
    else:
        my_list.append([c])
print(my_list)
