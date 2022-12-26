file = open("files/check.txt")
lines = file.readlines()

file.close()

lines = list(filter(None, (line.rstrip() for line in lines)))

parties_list = lines[lines.index("PARTIES:") + 1: lines.index("VOTES:")]
votes_list = lines[lines.index("VOTES:") + 1:]



count_voces_list = []
count_voces_list.append(votes_list.count('Party one'))
count_voces_list.append(votes_list.count('Party two'))
count_voces_list.append(votes_list.count('Party three'))

parties_and_votes = dict(zip(parties_list, count_voces_list))

total = sum(list(parties_and_votes.values()))

for party, votes in parties_and_votes.items():
    if votes >= 7 * total / 100:
        print(party)