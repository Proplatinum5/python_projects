def sent_is_palindrome(words):
    string = ""
    return string[::-1].casefold() == string.casefold()
def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return sent_is_palindrome(string)

word = "-"
while word != "0":

    word = input("Please enter a word: or select 0 to exit program ")


    if word == "0":
        print("We will now exit the program thank you")

    elif palindrome_sentence(word):
        print("'{}' is a palindrome".format(word))
    else:
        print("'{}' is not a palindrome".format(word))