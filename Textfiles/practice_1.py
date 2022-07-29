def capital_indexes(text: str) -> list:

    capital_positions = []
    for index, char in enumerate(text):
        if char.isupper():
            capital_positions += char
    print(capital_positions)




capital_indexes("Hello my name is Marry ")


