# Зашифруйте данный текстовый файл шифром Цезаря, при этом символы первой строки файла должны циклически сдвигаться на 1,
# второй строки — на 2, третьей строки — на три и т.д.
# В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.

file = open("check.txt")
line = file.readline().lower().rstrip('\n')

alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]  # lower

text = ''
for i in range(len(line)):
    if line[i] not in '.,!:"':
        text += line[i]

lst = text.split()

result = []
for el in lst:
    for ch in el:
        if ch in alphabet:
            result += chr((ord(ch) - ord("a") + len(text.split('\n')) % 26) + ord("a"))


print(''.join(result))
