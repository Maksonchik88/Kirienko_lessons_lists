file = open("dict/text.txt")
word_count = int(file.readline())
words_from_dictionary = {}
for _ in range(word_count):
    word = file.readline().rstrip()
    key_word = word.lower()
    if key_word not in words_from_dictionary:
        words_from_dictionary[key_word] = set()
    words_from_dictionary[key_word].add(word)
print(words_from_dictionary)
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
    lower_word = word.lower()
    if lower_word in words_from_dictionary and word not in words_from_dictionary[lower_word] and data_completed[
        word] > 1 or data_completed[word] == 0:
        mistakes += 1

print(mistakes)
