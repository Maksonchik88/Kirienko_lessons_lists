# Во входном файле записана одна текстовая строка, возможно, содержащая пробелы. Выведите эту строку в обратном порядке.
# Строка во входном файле заканчивается символом конца строки '\n'.


file = open("/home/max/projects/kirienko/files/check.txt")
a = file.read()
a = a.split()
a = reversed(a)
for i in a:
    i = i[::-1]
    print(i, end=' ')

file.close()
