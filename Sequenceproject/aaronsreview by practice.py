Cryptos = ["bitcoin",
           "eth",
           "amp",
           "dogecoin"]

valid_choices = []
for i in range(1, len(Cryptos) +1):
    valid_choices.append(str(i))
print(valid_choices)
current_choice = "-"
available_crypto = []

while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice) -1
        chosen_crypto = Cryptos[index]
        if chosen_crypto in available_crypto:
            print("removing {}".format(current_choice))
            available_crypto.remove(chosen_crypto)
        else:
            print("adding {}".format(current_choice))
            available_crypto.append(chosen_crypto)
        print("your list now contains:{}".format(available_crypto))
    else:
        print("Please add options from the list below:")
        for number, crypto in enumerate(Cryptos):
            print("{0}: {1}".format(number + 1, crypto))
    current_choice = input()

print(available_crypto)