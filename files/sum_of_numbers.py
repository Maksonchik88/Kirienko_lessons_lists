# Дан файл, каждая строка которого может содержать одно или несколько целых чисел, разделенных одним или несколькими пробелами.
# Вычислите сумму чисел в каждой строке и выведите эту сумму (для каждой строки выводится сумма чисел в этой строке).
# В данной задаче удобно считывать данные построчно. N неограниченно. Сумма чисел в каждой строке не превосходит 109.


file = open("/home/max/projects/kirienko/files/check.txt")
text = file.readlines()
for line in text:
    line = line.split()
    counter = 0
    for el in line:
        counter += int(el)
    print(counter)
