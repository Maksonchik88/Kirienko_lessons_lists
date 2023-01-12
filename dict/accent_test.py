file = open("dict/text.txt")
word_count = int(file.readline())
data = {}
for _ in range(word_count):
    word = file.readline().rstrip()
    key_word = word.lower()
    if key_word not in data:
        data[key_word] = [word]
    else:
        data[key_word].append(word)

print(data)

completed_exercise = file.readline().rstrip().split()
print(completed_exercise)
file.close()

data_completed = {}
for word in completed_exercise:
    letters_counter = 0
    for ch in word:
        if ch.isupper():
            letters_counter += 1
    if word not in data_completed:
        data_completed[word] = letters_counter
print(data_completed)
mistakes = 0
for word in completed_exercise:
    word_lower = word.lower()
    if data_completed[word] > 1 or data_completed[word] == 0:
        mistakes += 1
print(mistakes)
