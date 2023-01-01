file = open("files/check.txt")
num_of_sets = int(file.readline())
lines = file.readlines()

file.close()

scores_of_all_university_applicants = {}
did_not_pass_the_competition = {}
total_applicants = 0
total_did_not_applicants = 0
for line in lines:
        line_for_sorting = line.split()
        balls = list(map(int, line_for_sorting[-3:]))
        fullname = ' '.join(line_for_sorting[:-3])
        sum_balls = sum(balls)
        min_balls = min(balls)
        if min_balls < 40:
                total_did_not_applicants += 1
                if sum_balls not in did_not_pass_the_competition:
                        did_not_pass_the_competition[sum_balls] = []
                did_not_pass_the_competition[sum(balls)].append(fullname)
        elif min_balls >= 40:
                total_applicants += 1
                if sum_balls not in scores_of_all_university_applicants:
                        scores_of_all_university_applicants[sum_balls] = []
                scores_of_all_university_applicants[sum_balls].append(fullname)

scores_of_all_university_applicants_sort = sorted(scores_of_all_university_applicants.items(), reverse=True)
did_not_pass_the_competition_sort = sorted(did_not_pass_the_competition.items(), reverse=True)
print(scores_of_all_university_applicants_sort)
print(did_not_pass_the_competition_sort)

max_len_of_fullnames = 0
for elem in scores_of_all_university_applicants_sort:
        if len(elem[1]) > max_len_of_fullnames:
                max_len_of_fullnames = len(elem[1])

if total_applicants <= num_of_sets:
        print(0)
elif max_len_of_fullnames > num_of_sets:
        print(1)

for elem in scores_of_all_university_applicants_sort:
        if num_of_sets - 1 <= len(elem[1]) < num_of_sets:
                print(elem[0])
                break
        else:
                num_of_sets -= len(elem[1])