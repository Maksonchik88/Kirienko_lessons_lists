#Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа.
#Если соседних элементов одного знака нет - не выводите ничего.
#Если таких пар соседей несколько - выведите первую пару.

m = [int(i) for i in (input().split())]
for i in range(1, len(m)):
    if m[i] < 0 and  m[i - 1] < 0 or m[i] > 0 and  m[i - 1] > 0:
        print(m[i - 1], m[i],  end=' ')
        break
