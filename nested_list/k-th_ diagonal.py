#4
#1 2 3 4
#5 6 7 8
#0 1 2 3
#4 5 6 7
#1
n = int(input())
mtx = [list(map(int, input().split())) for i in range(n)]
k = int(input())
if k > 0:
    temp = 0
    for i in range(k, len(mtx)):
        print(mtx[i][temp], end=' ')
        temp += 1
elif k < 0:
    for i in range(0, len(mtx) - k - 1):
        print(mtx[i][i - k], end=' ')
else:
    for i in range(len(mtx)):
        print(mtx[i][i], end=' ')