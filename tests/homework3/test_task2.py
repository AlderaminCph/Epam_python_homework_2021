import time

from homework3.task2 import my_calculation, slow_calculate


def test_slow_calculate_perfomance_time():
    if __name__ == "__main__":
        time_begin = time.time()
        call_func(list(range(0, 501)), slow_calculate)
        time_end = time.time()
        assert time_end - time_begin < 60


def test_slow_calculate_result():
    if __name__ == "__main__":
        result = call_func(list(range(0, 501)), slow_calculate)
        assert 1025932 == result
