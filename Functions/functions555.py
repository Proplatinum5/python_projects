def multiply(x, y):
    """
    The function will return x multiplied by y
    :param x: The first number in the multiplication
    :param y: The second number in the multiplication
    :return:  The result of multiplying x and y
    """
    result = x * y
    return result
word = "-"
while word != "0":
    word = input("Please enter a word: or select 0 to exit program ")
    def is_palindrome(string):
        """
        Will return True if (string) is equal to (string) reversed
        :param string: Receives `str` to check if conditions of
            function are met.
        :return: Will return true if conditions of functions are met
        """
        #   backwards = string[::-1]
      #  return backwards == string
        return string[::-1].casefold() == string.casefold()


    def is_palindrom_sent(sentence):
        sent = ""
        for char in word:
            if char.isalnum():
                sent += char
        return is_palindrome(sent)


#
#   if word == "0":
#       print("We will now exit the program thank you")
#
#   elif is_palindrom_sent(word):
#       print("'{}' is a palindrome".format(word))
#
#   else:
#       print("'{}' is not a palindrome".format(word))
#

#def multiply(x, y):
#    """
#    Multiply 2 numbers.
#
#    Although this function is intended to multiply 2 numbers,
#    you can also use it to multiply a sequence.  If you pass
#    a string, for example, as the first argument, you'll get
#    the string repeated `y` times as the returned value.
#
#    :param x: The first number to multiply.
#    :param y: The number to multiply `x` by.
#    :return: The product of `x` and `y`.
#    """
#    result = x * y
#    return result
#
#
#def is_palindrome(string):
#    """
#    Check if a string is a palindrome.
#
#    A palindrome is a string that reads the same forwards as backwards.
#
#    :param string: The string to check.
#    :return: True if `string` is a palindrome, False otherwise.
#    """
#    return string[::-1].casefold() == string.casefold()
#
#
#def palindrome_sentence(sentence):
#    """
#    Check if a sentence is a palindrome.
#
#    The function ignores whitespace, capitalisation and
#    punctuation in the sentence.
#
#    :param sentence: The sentence to check.
#    :return: True if `sentence` is a palindrome, False otherwise.
#    """
#    string = ""
#    for char in sentence:
#        if char.isalnum():
#            string += char
#    return is_palindrome(string)

# This is the way they documented in the class however documentaion
# is more of a personal design and you can include what you think
# you need to include in documentaion to make it clear to readers
def fibonacci(n):
    """Return the `n`th Fibonacci number, for positive `n`."""
    if 0<= n <= 1:
        return n

    n_minu1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minu1
        n_minus2 = n_minu1
        n_minu1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))