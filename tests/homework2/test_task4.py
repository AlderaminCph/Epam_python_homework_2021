from unittest import mock

import pytest

from homework2.task4 import cache

args = [(1, 2), ("a", 2), (1)]
values = [1, 9, [3, 4, 5]]
vals = dict(zip(args, values))


def side_effect(arguments):
    return vals[arguments]


@pytest.mark.parametrize(
    "arguments", [args[0], args[1], args[0], args[1], args[0], args[2], args[2]]
)
def test_cache_several_arguments(arguments):
    print("Args=", arguments)
    mock_function = mock.Mock(side_effect=side_effect)
    input_function = mock_function
    mock_function = cache(mock_function)
    mock_function(arguments)
    assert input_function.call_count == 1
