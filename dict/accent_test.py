file = open("dict/text.txt")
word_count = int(file.readline())

words_from_dictionary = {}
for _ in range(word_count):
    word = file.readline().rstrip()
    key_word = word.lower()
    if key_word not in words_from_dictionary:
        words_from_dictionary[key_word] = set()
    words_from_dictionary[key_word].add(word)

completed_exercise = file.readline().rstrip().split()

file.close()

mistakes = 0
for word in completed_exercise:
    letters_counter = sum(1 for ch in word if ch.isupper())
    lower_word = word.lower()
    if letters_counter != 1 or (lower_word in words_from_dictionary
                                and word not in words_from_dictionary[lower_word]):
        mistakes += 1
print(words_from_dictionary)
print(completed_exercise)
print(mistakes)
