def stutter(word: str) -> str:
    stutter_word = word[0:3:1]
    complete_phrase = ("{}...{}...{}".format(stutter_word,stutter_word,word))
    return complete_phrase

print(stutter("Mommy"))

