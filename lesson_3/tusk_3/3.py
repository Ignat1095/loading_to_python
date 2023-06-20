# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
from string import punctuation, digits

file = open("3.txt", "r", encoding="utf-8")
text = file.read()


def clean_text(my_text: str, min_length: int = 0) -> list[str]:
    result = []
    punctuation_digits = punctuation + digits
    for i in punctuation_digits:
        my_text = my_text.replace(i, '')
    for word in my_text.split():
        word = word.lower()
        if len(word) >= min_length:
            result.append(word)
    return result


def counter(word_list: list[str]) -> dict[str, int]:
    count_dict = {}
    for word in word_list:
        count_dict[word] = count_dict.get(word, 0) + 1
    return count_dict


def words_counter(count_dict: dict[str, int], top: int) -> str:
    top_words = sorted(list(count_dict.items()), key=lambda x: x[1], reverse=True)[:top]
    words = [len(x[0]) for x in top_words]
    max_length = max(words)
    min_word = min(words)
    result = [f"Топ {top} слов в тексте с минимальной длинной в {min_word} букв: "]
    for i, word in enumerate(top_words, 1):
        result.append(f"{i:>2}. {word[0]:_<{max_length}} {word[1]:<3}")
    return '\n'.join(result)


print(words_counter(counter(clean_text(text, 4)), 10))
