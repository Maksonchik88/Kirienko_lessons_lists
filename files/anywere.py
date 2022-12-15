a = open("/home/max/projects/kirienko/files/check.txt")
a1 = a.read()
a1 = a1.split()
total = 0
for el in a1:
    total += int(el)
a.close()

b = open("/home/max/projects/kirienko/files/ans.txt", "a")
b.write(str(total))
b.close()

