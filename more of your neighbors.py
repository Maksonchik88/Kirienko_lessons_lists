#Дан список чисел.
# Определите, сколько в этом списке элементов,
# которые больше двух своих соседей и выведите количество таких элементов.

n = [int(i) for i in input().split()]
counter = 0
for i in range(1, len(n) - 1):
    if n[i] > n[i - 1] and n[i] > n[i + 1]:
        counter += 1
print(counter, sep=' ')
