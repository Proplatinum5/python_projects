v = ["a", "e", "i", "o", "u"]

word = input("please enter a word and i will extract all vowels")
vowels = []
for letter in word:
    if letter in v:
        vowels.append(letter)
        print(letter)
print(vowels)


