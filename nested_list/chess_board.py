#Даны два числа n и m.
# Создайте двумерный массив размером n×m и заполните его символами "." и "*" в шахматном порядке.
# В левом верхнем углу должна стоять точка.

n, m = [int(c) for c in input().split()]
lst = [['.'] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if not (i + j) % 2 == 0:
            lst[i][j] = '*'
for row in lst:
    print(' '.join(row))
