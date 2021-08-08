import os

import pytest

from homework4.task1 import read_magic_number


@pytest.fixture()
def create_input_file(file_path: str, value: str) -> None:
    """Create input file and write value to it

    Args:
        file_path: path to file
        value: value to write in file
    """
    with open(file_path, "w") as file:
        file.write(value)


@pytest.mark.parametrize(
    ["file_path", "value"],
    [
        ("data1.txt", "1.5"),
        ("data2.txt", "1"),
        ("data3.txt", "2.87\nsome word here\n24\n"),
        ("data4.txt", "1\n"),
    ],
)
def test_read_magic_number_positive_case(file_path, value, create_input_file):
    our_result = read_magic_number(file_path)
    os.remove(file_path)
    assert our_result is True


@pytest.mark.parametrize(
    ["file_path", "value"],
    [
        ("data1.txt", "-1"),
        ("data2.txt", "0"),
        ("data3.txt", "3\nsome words here\nsome information\n"),
        ("data4.txt", "0.999\n"),
    ],
)
def test_read_magic_number_negative_case(file_path, value, create_input_file):
    our_result = read_magic_number(file_path)
    os.remove(file_path)
    assert our_result is False


@pytest.mark.parametrize(
    ["file_path", "value"],
    [
        ("data1.txt", "some words here"),
        ("data2.txt", " "),
        ("data3.txt", ""),
        ("data4.txt", "\n"),
    ],
)
def test_read_magic_number_value_error(file_path, value, create_input_file):
    with pytest.raises(ValueError):
        read_magic_number(file_path)
    os.remove(file_path)
