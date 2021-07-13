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
from collections import defaultdict
from typing import List

from spacy.lang.de import German


def hlper_fnc(ele):
    """Get uniique elements count (helper function)"""
    return len(list(set(ele)))


def get_longest_diverse_words(file_path: str) -> List[str]:
    """Find 10 longest words consisting from largest amount of unique symbols.

    Args:
        file_path: path to the file
    Returns:
        List[str]: list containing 10 longest words with max amount of unique symbols.
    """
    nlp = German()
    with open(file_path, "r", encoding="unicode-escape") as file:
        german_text = file.read()
        doc = nlp(german_text)
        tokens = [token.text for token in doc]
        words = [toc for toc in tokens if unicodedata.category(toc[0]).startswith("L")]
        words.sort(key=hlper_fnc, reverse=True)
        ten_longest_unique_words = words[:10]
    return ten_longest_unique_words


def char_tokenize(input_file):
    """Split an entire text from input file into small units, also known as tokens.

    Args:
        input_file: file with text to tokenize
        char_tokenize_flag: if char_tokenize_flag = True tokenize characters
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
        yield char


def get_rarest_char(file_path: str) -> str:
    """Find rarest symbol for document.

    Args:
        file_path: path to the file
    Returns:
        rarest_char: string
    """
    with open(file_path, "r", encoding="unicode-escape") as file:
        chars_dict = defaultdict(int)
        for token in list(char_tokenize(file)):
            chars_dict[token] += 1
    return sorted(chars_dict.items(), key=lambda item: item[1])[0][0]


def count_punctuation_chars(file_path: str) -> int:
    """Count every punctuation char.

    Args:
        file_path: path to the file
    Returns:
        int: the number of punctuation characters
    """
    with open(file_path, "r", encoding="unicode-escape") as file:
        chars_counter = sum(
            1
            for token in list(char_tokenize(file))
            if unicodedata.category(token).startswith("P")
        )
    return chars_counter


def count_non_ascii_chars(file_path: str) -> int:
    """Count every non ascii char.

    Args:
        file_path: path to the file
    Returns:
        int: the number of  non ascii characters
    """
    with open(file_path, "r", encoding="unicode-escape") as file:
        chars_counter = sum(
            1
            for token in list(char_tokenize(file))
            if token.isascii() == False and token not in string.whitespace
        )
    return chars_counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    """Find most common non ascii char for document.

    Args:
        file_path: path to the file
    Returns:
        str: the most common non ascii char for document
    """
    with open(file_path, "r", encoding="unicode-escape") as file:
        chars_dict = defaultdict(int)
        for token in list(char_tokenize(file)):
            if token.isascii() == False and token not in string.whitespace:
                chars_dict[token] += 1
    return sorted(chars_dict.items(), reverse=True, key=lambda item: item[1])[0][0]
