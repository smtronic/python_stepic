# Напишите программу, которая с помощью модуля random перемешивает случайным образом содержимое матрицы (двумерного списка).
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

def matrix_shuffle(matrix):
    matrix = [[shuffle(matrix[i])] for i in range(len(matrix))]

matrix_shuffle(matrix)
