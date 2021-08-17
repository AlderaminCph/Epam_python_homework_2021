import pytest

from homework4.task3 import my_precious_logger


@pytest.mark.parametrize(
    ["text", "stdout_value", "stderr_value"],
    [
        ("OK", "OK", ""),
        ("error: file not found", "", "error: file not found"),
    ],
)
def test_my_precious_logger_positive(capfd, text, stdout_value, stderr_value):
    my_precious_logger(text)
    stdout, stderr = capfd.readouterr()
    assert stdout == stdout_value
    assert stderr == stderr_value
