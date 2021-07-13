from homework3.task1 import cache


def test_cashe():
    @cache(times=2)
    def func(args):
        return args

    assert func(10) == 10
    assert func(10) == 10
    assert func(5) == 5
    assert func(5) == 5
