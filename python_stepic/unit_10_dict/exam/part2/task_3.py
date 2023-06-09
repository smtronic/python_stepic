# Scrabble game
# В игре Scrabble каждая буква приносит определенное количество баллов. Общая стоимость слова – сумма баллов его букв. Чем реже буква встречается, тем больше она ценится:

# Баллы	Буква
# 11	AA, EE, II, LL, NN, OO, RR, SS, TT, UU
# 22	DD, GG
# 33	BB, CC, MM, PP
# 44	FF, HH, VV, WW, YY
# 55	KK
# 88	JJ, XX
# 1010	QQ, ZZ
# Напишите программу подсчета итоговой стоимости введенного слова.

# Формат входных данных
# На вход программе подается одно слово в верхнем регистре на английском языке.

# Формат выходных данных
# Программа должна вывести суммарную стоимость букв введеного слова.

dict = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
    }
result = 0
for char in input():
    for key, value in dict.items():
        if char in value:
            result += key
print(result)
