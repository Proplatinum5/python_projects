def multiply(x: float, y: float) -> float:
    result = x * y
    return result


def is_palindrome(string: str) -> bool:
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence: str) -> bool:
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)


# word = input("Please enter a word to check: ")
# if palindrome_sentence(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))

def fibonacci(n: int) -> int:
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


for i in range(int(input("please enter a number"))):
    print(i, fibonacci(i))

p = palindrome_sentence()