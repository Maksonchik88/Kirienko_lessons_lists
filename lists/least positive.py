#Выведите значение наименьшего из всех положительных элементов в списке.
# Известно, что в списке есть хотя бы один положительный элемент,
# а значения всех элементов списка по модулю не превосходят 1000.


lst = list(map(int, input().split()))
my_lst = []
for i in lst:
    if i > 0:
        my_lst.append(i)
print(min(my_lst))