import math


def convert(number):
    result = []

    i = 2
    while number != 0:
        number, mod = divmod(number, i)
        result.append(mod)
        i += 1

    result.reverse()
    return result + [0]


def convert_to_dec(array):
    result = 0

    factorial, tmp = 1, 1
    for item in reversed(array):
        result += item * factorial
        factorial *= tmp
        tmp += 1

    return result
