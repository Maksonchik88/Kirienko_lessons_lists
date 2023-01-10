action_on_a_file = {
    'read': 'R',
    'write': 'W',
    'execute': 'X'
}
print(action_on_a_file)
file = open("dict/text.txt")
count = int(file.readline())
data = {}
lines = file.readlines()[:count]

for line in lines:
    line_for_sort = line.split()
    name = line_for_sort[0]
    options = line_for_sort[1:]
    data[name] = options

count_2 = int(file.readline())
check_lines = file.readlines()[count_2:]

file.close()

for line in check_lines:
    action, file = line.split()
    if action_on_a_file[action] in data[file]:
        print("OK")
    else:
        print("Access denied")
