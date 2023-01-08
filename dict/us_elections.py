file = open("dict/text.txt")

data = {}
for line in file:
    name, votes = line.split()
    votes = int(votes)
    if name not in data:
        data[name] = votes
    data[name] += votes
for name, votes in data.items():
    print( name, votes)