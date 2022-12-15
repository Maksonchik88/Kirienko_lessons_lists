a = open("/home/max/projects/kirienko/files/check.txt")
a1 = a.read()
total = 0
for el in a1:
    if el in '0123456789':
        total += int(el)
a.close()

b = open("/home/max/projects/kirienko/files/ans.txt", "a")
b.write(str(total))

b.close()
