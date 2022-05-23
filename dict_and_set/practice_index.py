family = [
    ("Wilcox Family", "Tennessee",
    [
        (1, "Aaron"),
        (2, "EmilyM"),
        (3, "EmilyW"),
        (4, "Michael")
    ]
     ),
    ("Rock Family", "Ohio",
     [
        (1, "Leo"),
        (2, "Zion"),
        (3, "Aster")
        ]
     )]


def pull_famname(x: list):
    """
    Will pull str from indexed list containing names and location
    :param x:str name of list to apply function
    :return: returns desired str from indexed material
    """

    for index, (family_name, state, names) in enumerate(x):
        print("{}, {}, {}".format(index + 1, family_name, names))


pull_famname(family)