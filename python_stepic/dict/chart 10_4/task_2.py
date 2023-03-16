# Анаграммы 1
# Анаграмма – слово (словосочетание), образованное путём перестановки букв, составляющих другое слово (или словосочетание). Например, английские слова evil и live – это анаграммы.

# На вход программе подаются два слова. Напишите программу, которая определяет, являются ли они анаграммами.

# Формат входных данных
# На вход программе подаются два слова, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести YES если слова являются анаграммами и NO в противном случае.
# Sample Input 1:

# thing
# night
# Sample Output 1:

# YES

# from collections import Counter

# print('YES' if Counter(input()) == Counter(input()) else 'NO')

word = input()
word2 = input()
my_dict  = {char:word.count(char) for char in word}
my_dict2  = {char:word2.count(char) for char in word2}
print('YES' if my_dict == my_dict2 else 'NO')
