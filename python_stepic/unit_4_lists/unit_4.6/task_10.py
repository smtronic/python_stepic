# ; Заполнение спиралью 😈😈
# ; На вход программе подаются два натуральных числа
# ; n и m. Напишите программу, которая создает матрицу размером
# ; n×m заполнив её "спиралью" в соответствии с образцом.

# ; Формат входных данных
# ; На вход программе на одной строке подаются два натуральных числа
# ; n и m — количество строк и столбцов в матрице.

# ; Формат выходных данных
# ; Программа должна вывести матрицу в соответствии образцом.

# ; Примечание. Для вывода элементов матрицы как в примерах, отводите ровно
# ; 3
# ; 3 символа на каждый элемент. Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇



rows, cols = map(int, input().split())
matrix = [[0] * cols for _ in range(rows)]
index = 1
for i in range(rows):
        for j in range(i, cols - i -1):
            if index > rows * cols:
                break
            else:
                matrix[i][j] = index
                index += 1
        for j in range(i, rows - i - 1):
            if index > rows * cols:
                break
            else:
                matrix[j][cols - i - 1] = index
                index += 1
        for j in range(cols - i - 1, i, - 1):
            if index > rows * cols:
                break
            else:
                matrix[rows - i - 1][j] = index
                index += 1
        for j in range(rows - i - 1, i, -1):
            if index > rows * cols:
                break
            else:
                matrix[j][i] = index
                index += 1
if rows % 2 == 1 and cols % 2 == 1 and rows == cols:
    matrix[rows // 2][cols // 2] = index

for i in range(rows):
    for j in  range(cols):
        print(str(matrix[i][j]).ljust(5), end ='')
    print()
