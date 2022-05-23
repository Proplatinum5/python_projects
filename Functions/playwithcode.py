def factorial(n: int) -> int:
    """
    Take an argument and will make a factorial up to that number
    a factorial is multiplying all number from 1 to x in this
    situation.
    :param x: x is the number you wish to create a factorial on
    :return: will return ints of all numbers in factorials multiplied
    in order

    """

    if n <= 1:
        return 1

    result = 2
    for x in range(3, n + 1):
        result *= x

    return result


for i in range(36):
    print(i, factorial(i))
