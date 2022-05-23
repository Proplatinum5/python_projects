def fizz_buzz(x):
    """
    takes input and calculates if x is divisible by 3, 5, or both
    :param x: number you want to be divided by if factors
    :return:returns text Fizz Buzz or FIZZBUZZ if the modular factor
    returns true to being zero
    """

    if x % 15 == 0:
        return "FIZZ BUZZ"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return str(x)

input("play fizz buzz")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)

#    players_answer = input("your go")
    players_answer = correct_answer
    if players_answer != correct_answer:
        print("you lose")
        break
else:
    print("well done, you reached {}".format(next_number))



