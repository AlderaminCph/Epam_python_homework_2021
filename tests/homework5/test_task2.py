import functools

import pytest

from homework5.task2 import new_decorator, print_result


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)


def test_doc_and_name():
    assert (
        custom_sum.__doc__
        == """This function can sum any objects which have __add___"""
    )
    assert custom_sum.__name__ == "custom_sum"


def test_print_result_stdout(capfd):
    custom_sum([1, 2, 3], [4, 5])
    stdout, stderr = capfd.readouterr()
    assert stdout == "[1, 2, 3, 4, 5]\n"
    assert stderr == ""


def test_print_result_without_print(capfd):
    without_print = custom_sum.__original_func
    stdout, stderr = capfd.readouterr()
    assert without_print(1, 2, 3, 4) == 10
    assert stdout == ""
    assert stderr == ""
