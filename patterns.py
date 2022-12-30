file = ["a", "b", "c", "a", "c", "a", "b", "e"]

# 1 Аггрегация
# 1.1 Частота

data = {}
for line in file:
    if line not in data:
        data[line] = 0
    data[line] += 1
print(data)

# {'a': 3, 'b': 2, 'c': 2, 'e': 1}

# 1.2 Список

# {'a': [0, 3, 5], 'b': [1, 6], 'c': [2, 4], 'e': [7]}

data2 = {}
for i in range(len(file)):
    line = file[i]
    if line not in data2:
        data2[line] = []
    data2[line].append(i)
print(data2)

# 1.3. Сумма/Максимум/Минимум

# [('a', 5), ('b', 4), ('a', 3), ('a', 1), ('c', 2), ('b', 2)]
# SUM -> {'a': 9, 'b': 6, 'c': 2}
# MAX -> {'a': 5, 'b': 4, 'c': 2}
# MIN -> {'a': 1, 'b': 2, 'c': 2}

# 2. Реверс
data_rev = {}
for key, value in data.items():
    if value not in data_rev:
        data_rev[value] = []
    data_rev[value].append(key)
print(data_rev)


# 3. Поиск второго максимума (первого и второго максимума)
source = [1, 12, 3, 6, 8, 10, 6]
first_max = 0
second_max = 0
for el in source:
    if first_max < el:
        second_max = first_max
        first_max = el
    elif second_max < el:
        second_max = el
print(first_max, second_max)

# 4. Поиск максимума по значению словаря (не по ключу)
max_val = 0
max_key = None
for key, value in data.items():
    if value > max_val:
        max_val = value
        max_key = key
print(max_key, data[max_key])


# Вычислительная сложность алгоритма
"""
n = количество элементов
вот что можно почитать https://tproger.ru/articles/computational-complexity-explained/

O(1) - константная (доступ к элементу словаря)
O(log(n)) - логарифмическая (бинарный поиск элемента в отсортированном списке)
O(n) - линейная (поиск элемента в  списке, полный перебор/итерирование) 
O(n * log(n) - сортировка
O(n**2) - квадратичная (полиномиальная) - 2 вложенных for (поиск элемента в матрице)
O(n**3) - квадратичная (кубическая) - 3 вложенных for (поиск элемента в 3d матрице)
O(n!) - факториал
O(exp(n)) - экспоненциальная
"""