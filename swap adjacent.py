#Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т.д.).
# Если элементов нечетное число, то последний элемент остается на своем месте.



lst = [int(i) for i in input().split()]
if len(lst) % 2 == 0:
    for i in range(1, len(lst), 2):
        lst[i], lst[i-1] = lst[i - 1], lst[i]
elif len(lst) % 2 != 0:
    for j in range(1, len(lst) - 1, 2):
        lst[j], lst[j - 1] = lst[j - 1], lst[j]
print(*lst)
