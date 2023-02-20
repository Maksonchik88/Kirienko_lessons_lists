file = open("dict/test.txt")
number_of_elements_in_the_tree = int(file.readline())

many_vertices = set()
dependency_dictionary = {}
for line in range(number_of_elements_in_the_tree - 1):
    line = file.readline()
    descendant, parent = line.split()
    many_vertices.add(descendant)
    many_vertices.add(parent)
    if parent not in dependency_dictionary:
        dependency_dictionary[parent] = [descendant]
    else:
        dependency_dictionary[parent].append(descendant)

file.close()

values_list = []
for name_list in dependency_dictionary.values():
    for name in name_list:
        values_list.append(name)

queue = []
for name in many_vertices:
    if name not in values_list:
        queue.append(name)

level = 0
generations = {}
while len(queue) > 0:
    temp = []
    for a_person in queue:
        generations[a_person] = level
        if a_person in dependency_dictionary:
            children = dependency_dictionary[a_person]
            temp.extend(children)
    queue = temp
    level += 1

generations_sort = sorted(generations.items())
for ruler, level in generations_sort:
    print(ruler, level)


