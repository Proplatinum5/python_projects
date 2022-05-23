available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "hdmi cable",
                   "dvd drive"
                   ]
# valid_choices = [str(i) for i in range(1, len(available_parts) +1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)  # This is just for testing
current_choice = "-"
computer_parts = []  # create an empty list

available_parts.sort()

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
        seperator = " | "
        output = seperator.join(computer_parts)
        print("your list now contains: {}".format(output))
    else:
        print("Please add options from the list below:")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))
    current_choice = input()
seperator = " | "
output = seperator.join(computer_parts)
print(output)


# for part in available_parts:
# print("{0}: {1}".format(available_parts.index(part)+1, part))
