import mock
import pytest

from homework2.task4 import cache


def test_cache():
    mock_function = mock.Mock()
    input_function = mock_function
    mock_function = cache(mock_function)
    mock_function()
    mock_function()
    assert input_function.call_count == 1
