#В списке все элементы различны.
# Поменяйте местами минимальный и максимальный элемент этого списка.


a = [int(i) for i in input().split()]
maxi = a.index(max(a))
mini = a.index(min(a))
if len(a) > 0:
    a[maxi], a[mini]=a[mini], a[maxi]
print(' '.join([str(i) for i in a]))