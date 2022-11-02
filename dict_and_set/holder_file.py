def are_equal(contain_what: str) -> bool:
    """
    A simple function that takes in a str as a value and returns true if
    the amount of xs and os are equal, false if not.
    :param contain_what: a str that is counted (x, o)
    :return: Bool value True or False
    """
    o_amount = contain_what.count("o".casefold())
    x_amount = contain_what.count("x".casefold())

    if o_amount == x_amount:
        return True
    else:
        return False


print(are_equal("xxxxxxxxxxxxo"))






