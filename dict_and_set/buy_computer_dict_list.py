available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "HDMI cable",
                   "6": "dvd drive"
                   }

parts_list = []
current_choice = None
while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if available_parts[current_choice] in parts_list:
            print(f"removing {chosen_part}")
            parts_list.remove(chosen_part)
        else:
            print(f"Adding {chosen_part}")
            parts_list.append(chosen_part)
            print(f"your list now contains {parts_list}")


    else:
        print("Please add options from the list")
        # if current_choice not in available_parts: this was redundant code
        for key, value in available_parts.items():
            print(f"{key}: {value}")
        print("0: to finish")
    current_choice = input("> ")
print(parts_list)


