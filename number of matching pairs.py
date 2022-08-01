#Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.



lst = input().split()
counter = 0
for i in range(0, len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] == lst[j]:
            counter += 1
print(counter)
