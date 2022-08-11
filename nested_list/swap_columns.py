# Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j
# Программа получает на вход размеры массива n и m, затем элементы массива, затем числа i и j.
# Выведите результат. Решение оформите в виде функции SwapColumns (A, i, j).
# 3 4
# 11 12 13 14
# 21 22 23 24
# 31 32 33 34
# 0 1



def swap_columns(A, i, j):
    for f in range(len(lst)):
        A[f][i], A[f][j] = A[f][j], A[f][i]







n , m = [int(c) for c in input().split()]
lst = []
for i in range(n):
        elem = [int(k) for k in input().split()]
        lst.append(elem)
p, v = [int(p) for p in input().split()]

swap_columns(lst, p, v)

for col in lst:
    for el in col:
        print(el, end=' ')
    print()