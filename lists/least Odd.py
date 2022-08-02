        #Выведите значение наименьшего нечетного элемента списка,
        # а если в списке нет нечетных элементов - выведите число 0.

lst = [int(i) for i in input().split()]
lst2 = []
for c in lst:
    if c % 2 != 0:
        lst2.append(c)

if len(lst2) == 0:
    print('0')
else:
    print(min(lst2))