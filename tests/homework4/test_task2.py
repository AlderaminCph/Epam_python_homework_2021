import os
import urllib.request
from unittest.mock import MagicMock, patch

import pytest

from homework4.task2 import count_dots_on_i


@patch("urllib.request.urlopen")
def test_count_dots_on_i(mock_request):
    with open(
        os.path.dirname(os.path.abspath(__file__)) + "/wiki.html", "r"
    ) as input_file:
        html = input_file.read().encode()
    cm = MagicMock()
    cm.read.return_value = html
    cm.__enter__.return_value = cm
    mock_request.return_value = cm

    with urllib.request.urlopen("https://example.com/") as response:
        assert count_dots_on_i("https://example.com/") == 9239


def test_count_dots_on_i_error():
    with pytest.raises(ValueError):
        count_dots_on_i("incorrect_address")
