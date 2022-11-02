def capital_indexs(user_input: str) -> list:
    index_list = []
    for index, letter in enumerate(user_input):
        if letter.isupper():
            index_list.append(index)
    return index_list

print(capital_indexs("I Want To go To the Store"))
