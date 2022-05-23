menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]


for sandwhich in menu:
    for index in range(len(sandwhich) - 1, -1, -1):
        if sandwhich[index] == "spam":
            del sandwhich[index]
    print(", ".join(sandwhich))