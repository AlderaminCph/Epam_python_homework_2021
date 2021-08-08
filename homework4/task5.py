"""
This task is optional.
Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation in this video**.
Definition of done:
 - function is created
 - function is properly formatted
 - function has tests
>>> list(fizzbuzz(5))
["1", "2", "fizz", "4", "buzz"]
* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""
from typing import Generator, List


def fizzbuzz(n: int) -> Generator[str]:
    """Generator that takes a number N as an input
    and returns a generator that yields N FizzBuzz numbers

    Args:
        n: number
    Returns:
        generator
    """
    generator = infinite_fizzbuzz()
    for _ in range(n):
        yield next(generator)


def infinite_fizzbuzz():
    i = 0
    while True:
        for element in generate_fizzbuzz_cycle(begin_elemnt=i * 15):
            yield element
        i += 1


def generate_fizzbuzz_cycle(begin_elemnt):
    yield begin_elemnt + 1
    yield begin_elemnt + 2
    yield "fizz"
    yield begin_elemnt + 4
    yield "buzz"
    yield "fizz"
    yield begin_elemnt + 7
    yield begin_elemnt + 8
    yield "fizz"
    yield "buzz"
    yield begin_elemnt + 11
    yield "fizz"
    yield begin_elemnt + 13
    yield begin_elemnt + 14
    yield "fizzbuzz"
