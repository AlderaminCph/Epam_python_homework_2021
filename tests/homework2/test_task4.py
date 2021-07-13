from unittest import mock

import pytest

from homework2.task4 import cache

vals = {(1, 2): 1, ("a", 2): 9}


def side_effect(*args):
    return vals[args]


def test_cache_several_arguments():
    mock_function = mock.Mock(side_effect=side_effect)
    input_function = mock_function
    mock_function = cache(mock_function)
    mock_function(*list(vals.keys())[0])
    mock_function(*list(vals.keys())[0])
    assert input_function.call_count == 1


def test_cache_different_types_arguments():
    mock_function = mock.Mock(side_effect=side_effect)
    input_function = mock_function
    mock_function = cache(mock_function)
    mock_function(*list(vals.keys())[1])
    mock_function(*list(vals.keys())[1])
    assert input_function.call_count == 1


def test_cashe_without_arguments():
    mock_function = mock.Mock()
    input_function = mock_function
    mock_function = cache(mock_function)
    mock_function()
    mock_function()
    assert input_function.call_count == 1
