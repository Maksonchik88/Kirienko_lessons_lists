from typing import List


def get_read_file(file: str) -> List:  # читаем весь файл и возвращаем его списком
    file = open(file)
    lst = file.readlines()
    file.close()
    return lst


def make_dict(lst: list) -> dict:  # инициализируем словарь с возможными вариантами ударений
    my_dict = {}
    for st in lst:
        st = st.rstrip()
        key_word = st.lower()
        my_dict.setdefault(key_word, set()).add(st)
    return my_dict


def find_mistakes(lst: list) -> int:  # подсчитываем количество ошибок
    mistakes = 0
    for word in list_for_check:
        if check_word(word):
            mistakes += 1
    return mistakes


def check_word(word: str) -> bool:  # проверяем ударения для каждого слова проверочной строки
    letters_counter = sum(1 for ch in word if ch.isupper())
    if letters_counter != 1 or (word.lower() in make_dict(my_list) and word not in make_dict(my_list)[word.lower()]):
        return True

if __name__ == '__main__':
    my_list = get_read_file("text.txt")  # инициализируем список со словами для словаря
    list_for_check = my_list[-1].split()  # инициализируем список строк для проверки
    print(find_mistakes(list_for_check))


# file = open("text.txt")
# word_count = int(file.readline())
#
# words_from_dictionary = {}
# for _ in range(word_count):
#     word = file.readline().rstrip()
#     key_word = word.lower()
#     if key_word not in words_from_dictionary:
#         words_from_dictionary[key_word] = set()
#     words_from_dictionary[key_word].add(word)
#
# completed_exercise = file.readline().rstrip().split()
#
# file.close()
#
# mistakes = 0
# for word in completed_exercise:
#     letters_counter = sum(1 for ch in word if ch.isupper())
#     lower_word = word.lower()
#     if letters_counter != 1 or (lower_word in words_from_dictionary
#                                 and word not in words_from_dictionary[lower_word]):
#         mistakes += 1
#
# print(mistakes)
