#Дан список. Не изменяя его и не используя дополнительные списки, определите,
# какое число в этом списке встречается чаще всего.
# Если таких чисел несколько, выведите любое из них.



lst = [int(c) for c in input().split()]
temp = ''
counter = 0
for i in range(len(lst)):
    count = 0
    for j in range(len(lst)):
        if lst[i] == lst[j]:
            count += 1
    if count > counter:
        counter = count
        temp = lst[i]
    count = 0
print(temp)