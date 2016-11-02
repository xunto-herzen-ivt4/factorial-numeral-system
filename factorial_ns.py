import math


def convert(number):
    if number == 0:
        return [0]

    factorials = []
    next_fac = 1

    tmp = 2
    while next_fac <= number:
        factorials.append(next_fac)
        next_fac = factorials[-1] * tmp
        tmp += 1

    result = []
    for factorial in reversed(factorials):
        if number >= factorial:
            result.append(math.floor(number / factorial))
            number %= factorial
        else:
            result.append(0)

    return result


def convert_to_dec(array):
    result = 0

    factorial, tmp = 1, 2
    for item in reversed(array):
        result += item * factorial
        factorial *= tmp
        tmp += 1

    return result
