# Магический квадрат 🌶️
# Магическим квадратом порядка
# n называется квадратная таблица размера
# n×n, составленная из всех чисел
# 1,2,3,…,n
# так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой. Напишите программу, которая проверяет, является ли заданная квадратная матрица магическим квадратом.

# Формат входных данных
# На вход программе подаётся натуральное число
# n — количество строк и столбцов в матрице, затем элементы матрицы:
# n строк, по
# n чисел в каждой, разделённые пробелами.

# Формат выходных данных
# Программа должна вывести слово YES, если матрица является магическим квадратом, и слово NO в противном случае.

def magicmatrix(matrix, n):
        count = [i for i in range(1, (n * n) + 1)]
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 0:
                    return 'NO'
                if matrix[i][j] not in count:
                    return 'NO'
                else:
                    count.remove(matrix[i][j])

        total_row = [sum(matrix[i]) for i in range(n)]
        total_colum = [sum([matrix[j][i] for j in range(n)]) for i in range(n)]
        total_main_diag = sum([matrix[i][i] for i in range(n)])
        total_sidediag = sum([matrix[i][n-i-1] for i in range(n)])
        if total_row[i] == total_colum[i] == total_main_diag == total_sidediag:
            flag =  'yes'
        else:
            return 'NO'

        for i in range(1, n):
            if total_row[i] != total_row[i-1]:
                return 'NO'
            if total_colum[i] != total_colum[i-1]:
                return 'NO'
        else:
            return 'YES'

n = int(input())
list = [[int(i) for i in input().split()] for i in range(n)]


print(magicmatrix(list, n))
