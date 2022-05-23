low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("press enter to start")
guesses = 1

while low != high:
    print("\tGuessing in the range of {} and {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower"
                     "Enter h or l, or c if my guess was correct"
                     .format(guess)).casefold()
    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("That was not an option you twat now pick H L or C like come tf on read "
              "the freaking instructions")

   # guesses = guesses + 1
    guesses += 1
else:
    print("you thought of the number {}".format(low))
    print("I got it in {} guesses".format(guesses))