def checkio(number: int) -> int:
    import functools
    import operator
    a = []
    for x in str(number):
        n = int(x)
        if not n:
            continue
        else:
            a.append(n)
    res = functools.reduce(operator.mul, a)
    return res


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")