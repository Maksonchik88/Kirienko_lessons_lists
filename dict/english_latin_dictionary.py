file = open("dict/text.txt")
file.readline()
lines = file.readlines()

file.close()

en_data = {}
for line in lines:
    line = line.replace(' -', '').rstrip().replace(',', '')
    english, *latin = line.split()
    for mean in latin:
        if mean not in en_data:
            en_data[mean] = [english]
        else:
            en_data[mean].append(english)

en_data_sort = sorted(en_data.items())

for latin, english in en_data_sort:
        print(latin, '-', ', '.join(english))
