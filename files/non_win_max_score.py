file = open('files/check.txt')
my_dict = {}
for line in file:
    key, value = line.split()[2:]
    key, value = int(key), int(value)
    if key not in my_dict:
        my_dict[key] = [value]
    else:
        my_dict[key].append(value)
my_list = sorted(my_dict.items())
for k, v in my_list:
    max_val = 0
    pre_max = 0
    for num in v:
        if num > max_val:
            pre_max = max_val
            max_val = num
        elif num > pre_max:
            pre_max = num

    print(pre_max, end=' ')

