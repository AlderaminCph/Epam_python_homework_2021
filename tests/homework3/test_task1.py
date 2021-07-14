from homework3.task1 import cache


def test_cashe():
    @cache(times=2)
    def func(args):
        return args*2

    assert func(10) == 20
    assert func(10) == 20
    assert func(10) == 20
    assert func(5) == 10
    assert func(5) == 10
