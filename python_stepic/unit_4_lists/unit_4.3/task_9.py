# Список по образцу 2
# На вход программе подается число n. Напишите программу, которая создает и выводит построчно вложенный список, состоящий из
# n списков [[1], [1, 2], [1, 2, 3], ..., [1, 2, ..., n]].

# Формат входных данных
# На вход программе подается натуральное число n.

# Формат выходных данных
# Программа должна вывести построчно указанный вложенный список.# n = int(input())


print(*[list(range(1, i + 1)) for i in range(1, int(input()) + 1)] , sep = '\n')


#---------------2 вариант

my_list = []

for i in range(1, n + 1):
    my_list.append(list(range(1, i + 1)))

print(*my_list, sep = '\n')