# В файле могут быть записаны десятичные цифры и все, что угодно. Числом назовем последовательность цифр, идущих
# подряд (т.е. число всегда неотрицательно).
# Вычислите сумму всех чисел, записанных в файле. В данной задаче удобно считывать данные посимвольно.
file = open("check.txt")
text = file.readlines()
total = 0
cur = ''
for line in text:
    for ch in line:
        if ch.isdigit():
            cur += ch
        elif cur != '':
            total += int(cur)
            cur = ''
    if cur != '':
        total += int(cur)
print(total)