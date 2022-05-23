available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "HDMI cable",
                   "dvd drive"
                   ]
#valid_choices = [str(i) for i in range(1, len(available_parts) +1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)
current_choice = "-"
computer_parts = [] #create an empty list
seperator = " | "
output = seperator.join(available_parts)

while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            # it's already in, so remove it
            print("removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("addding {}".format(current_choice))
            computer_parts.append(chosen_part)

        print("your list now contains: {}".format(computer_parts))
    else:
        print("Please add options from the list below:")
        seperator = " | "
        selection = seperator.join(available_parts)
        for number, part in enumerate(selection):
            print("{0}: {1}".format(number + 1, part))
    current_choice = input()

print(output)













