"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import string
import unicodedata
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    """Find 10 longest words consisting from largest amount of unique symbols.

    Args:
        file_path: path to the file
    Returns:
        List[str]: list containing 10 longest words with max amount of unique symbols.
    """
    with open(file_path, "r", encoding="unicode-escape") as file:
        Ten_longest_unique_words = ["" for x in range(10)]
        for token in list(tokenizer(file, 0)):
            if token[0] == "word":
                for i, word in enumerate(Ten_longest_unique_words):
                    if token[1] not in Ten_longest_unique_words and len(
                        set(token[1])
                    ) > len(set(word)):
                        Ten_longest_unique_words[i] = token[1]
    return Ten_longest_unique_words


def tokenizer(input_file, char_tokenize_flag):
    """Split an entire text from input file into small units, also known as tokens.

    Args:
        input_file: file with text to tokenize
        char_tokenize_flag: if char_tokenize_flag = 1 tokenize characters
    Returns:
        tokens with their type (word, punctuation or whitespace) and value
    """
    buffer = ""
    char = " "
    while char:
        try:
            char = input_file.read(1)
        except:
            continue
        if not char:
            break
        if char_tokenize_flag == 1:
            yield char
        else:
            if unicodedata.category(char).startswith("P"):
                if buffer:
                    yield ("word", buffer)
                    buffer = ""
                yield ("punctuation", char)
                continue
            if char in string.whitespace:
                if buffer:
                    yield ("word", buffer)
                    buffer = ""
                yield ("whitespace", char)
                continue
            buffer += char
        if buffer:
            yield ("word", buffer)


def get_rarest_char(file_path: str) -> str:
    """Find rarest symbol for document.

    Args:
        file_path: path to the file
    Returns:
        rarest_char: string
    """
    with open(file_path, "r", encoding="unicode-escape") as file:
        chars_dict = dict()
        for token in list(tokenizer(file, 1)):
            if token in chars_dict:
                chars_dict[token] += 1
            else:
                chars_dict[token] = 1
    return sorted(chars_dict.items(), key=lambda item: item[1])[0][0]


def count_punctuation_chars(file_path: str) -> int:
    """Count every punctuation char.

    Args:
        file_path: path to the file
    Returns:
        int: the number of punctuation characters
    """
    with open(file_path, "r", encoding="unicode-escape") as file:
        chars_counter = 0
        for token in list(tokenizer(file, 1)):
            if unicodedata.category(token).startswith("P"):
                chars_counter += 1
    return chars_counter


def count_non_ascii_chars(file_path: str) -> int:
    """Count every non ascii char.

    Args:
        file_path: path to the file
    Returns:
        int: the number of  non ascii characters
    """
    with open(file_path, "r", encoding="unicode-escape") as file:
        chars_counter = 0
        for token in list(tokenizer(file, 1)):
            if token.isascii() == False and token not in string.whitespace:
                chars_counter += 1
    return chars_counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    """Find most common non ascii char for document.

    Args:
        file_path: path to the file
    Returns:
        str: the most common non ascii char for document
    """
    with open(file_path, "r", encoding="unicode-escape") as file:
        chars_dict = dict()
        for token in list(tokenizer(file, 1)):
            if token.isascii() == False and token not in string.whitespace:
                if token in chars_dict:
                    chars_dict[token] += 1
                else:
                    chars_dict[token] = 1
    return sorted(chars_dict.items(), reverse=True, key=lambda item: item[1])[0][0]


# print(get_longest_diverse_words("data.txt"),get_rarest_char("data.txt"),count_punctuation_chars("data.txt"),count_non_ascii_chars("data.txt"),get_most_common_non_ascii_char("data.txt"))
