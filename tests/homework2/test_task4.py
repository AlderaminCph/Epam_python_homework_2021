from unittest import mock

import pytest

from homework2.task4 import cache


def getArgStr(args, kwargs):
    return str(args) + ", " + str(kwargs)


args = [(5, 6), (2, "someStr", [2, 3, 4])]
kwargs = [{"k": 7}, {"qwert": [2, 3], "a": 9}]
results = [3, 7]

values = dict(zip((map(getArgStr, args, kwargs)), results))


def side_effect(args, kwargs):
    return values[getArgStr(args, kwargs)]


@pytest.mark.parametrize(
    "arguments, kwargs",
    [
        (args[0], kwargs[0]),
        (args[1], kwargs[1]),
        (args[0], kwargs[0]),
        (args[1], kwargs[1]),
        (args[0], kwargs[0]),
    ],
)
def test_cache_several_arguments(arguments, kwargs):
    mock_function = mock.Mock(side_effect=side_effect)
    mock_function.__name__ = "foo"
    input_function = mock_function
    mock_function = cache(mock_function)
    mock_function(arguments, kwargs)
    assert input_function.call_count == 1


def test_cashe_without_arguments():
    mock_function = mock.Mock()
    mock_function.__name__ = "foo"
    input_function = mock_function
    mock_function = cache(mock_function)
    mock_function()
    mock_function()
    assert input_function.call_count == 1
