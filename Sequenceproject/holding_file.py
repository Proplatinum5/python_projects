available_parts = [("computer", 457.23),
                   ("monitor", 129.87),
                   ("keyboard", 68.25),
                   ("mouse", 32.66),
                   ("HDMI cable", 20.99),
                   ("dvd drive", 120.25),
                   ]

valid_choices = []
selection = input("enter a number")
part = available_parts[int(selection)]
print(part)
for index, (part, price) in enumerate(available_parts):
    valid_choices.append((index, (part, price)))
#    print("Item #{}, Part: {}, Price: {}".format(index + 1, part, price))

print(valid_choices)
current_choice = "-"
computer_parts = []

while current_choice != '0':

    if current_choice in available_parts:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            print("removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("adding {}" .format(current_choice))
            computer_parts.append(chosen_part)
        print("your list now contains: {}".format(computer_parts))
    else:
        print("Please add options from the list below:")
        for index, (part, price) in enumerate(available_parts):
            print("{0}: {1}".format(index + 1, (part, price)))
    current_choice = input()
print(part)

