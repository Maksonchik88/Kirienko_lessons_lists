#Дано число n и массив размером n×n. Проверьте,
# является ли этот массив симметричным относительно главной диагонали.
# Выведите слово “YES”, если массив симметричный, и слово “NO” в противном случае.



def is_symmetrical(my_list):
    for i in range(n):
        for j in range(n):
            if my_list[i][j] != my_list[j][i]:
                return False
    return True



n = int(input())

lst = [list(map(int, input().split())) for c in range(n)]


if is_symmetrical(lst):
    print('YES')
else:
    print('NO')


