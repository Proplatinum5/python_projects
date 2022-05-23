import random

highest = 10
answer = random.randint(1, highest)


print("Please guess number between 1 and 10: ")
guess = int(input())
if guess == answer:
    print("congrats you got it on the first time")

while answer != guess:
    if guess == 0:
        print("You have chosen to stop the game and quit"
              " ... your a quitter how does that make you feel you are a "
              "disappointment to your family.")
        break
    elif guess < answer:
        print("please guess higher")
    else:  # guess must be greater than you anwser
        print("please guess lower")

    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("well done, you guessed it")
#     else:
#         print("Sorry you have not gueesed correctly ")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("well done, you guessed it")
#     else:
#         print("Sorry you have not guessed correctly ")
# else:
#     print("You got it the first time great job")
