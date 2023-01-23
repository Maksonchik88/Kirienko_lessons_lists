file = open("dict/text.txt")
number_of_states = int(file.readline())

states_and_electors = {}
for line in range(number_of_states):
    state_name, number_of_electors = file.readline().split()
    number_of_electors = int(number_of_electors)
    if state_name not in states_and_electors:
        states_and_electors[state_name] = number_of_electors
print(states_and_electors)
end_part_of_file = file.readlines()

file.close()

results_for_each_participant = {}
for line in end_part_of_file:
    state, candidate = line.split()
    if state not in results_for_each_participant:
        results_for_each_participant[state] = {candidate: 1}
    else:
        results_for_each_participant[state][candidate] = results_for_each_participant[state].get(candidate, 0) + 1
print(results_for_each_participant)
candidates_list = []
for state, candidate_count in results_for_each_participant.items():
    candidate_count_sort = sorted(candidate_count.items(), key=lambda x: (-x[1], x[0]))
    print(candidate_count_sort)
    print(candidate_count_sort[0][0], states_and_electors[state])
    candidates_list.append(candidate_count_sort[0][0])
print(candidates_list)
total_votes = {}
