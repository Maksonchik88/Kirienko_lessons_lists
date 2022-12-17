file = open('check.txt')
my_dict = {}
for line in file:
    key, value = line.split()[2:]
    if int(key) not in my_dict:
        my_dict[int(key)] = [int(value)]
    else:
        my_dict[int(key)].append(int(value))
for el in my_dict.values():
    max_val = max(el)
    for num in el:
        if num == max_val and el == []:
            print(max_val)
        elif num < max_val:
            print(num, end=' ')
