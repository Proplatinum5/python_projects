# Challenge pulling vowels out of a string
v = ["a", "e", "i", "o", "u"]

word = input("please enter a word and i will extract all vowels")
vowels = []
for letter in word:
    if letter in v:
        vowels.append(letter)
        print(letter)
print(vowels)

#   Challenge accept a credit card number and return the last four digits
credit_info = []

while True:


    customer_cc = input("Please enter your credit card number")


# I seem to be missing something why can I not iterate over the string
# inside the list backwards works forward just fine but won't go backwards.
# I will save that issue for another time.
    print((customer_cc[12:16]))

    cus_anws = input(" are these the last four of your card number?").casefold()
    if cus_anws == "yes":
        print("okay")
        credit_info.append(customer_cc)
    elif cus_anws == "no":
        credit_info.remove(customer_cc)
        print("removing number, thankyou for your input")
    else:
        print("you need to make a valid selection please type yes or no to the"
              "question provided, Thank you!")
    print(credit_info)
    print()
    print(" THEHEHHEHHE i will steal every ones credit card numbers mwahahhahahahah")
    print("Just kidding :)")

# def are_equal(contain_what: str) -> bool:
#   """
#   A simple function that takes in a str as a value and returns true if
#   the amount of xs and os are equal, false if not.
#   :param contain_what: a str that is counted (x, o)
#   :return: Bool value True or False
#   """
#   o_amount = contain_what.count("o".casefold())
#   x_amount = contain_what.count("x".casefold())
#
#   if o_amount == x_amount:
#       return True
#   else:
#       return False
#


