from contents import pantry, recipes

# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}
display_dict = {}
shopping_list = {}


def add_to_slist(data: dict, item: str, amount: int) -> None:
    """
    Function simply adds a key value pair from this program and inserts it
    into the dict.
    :return: None
    """
#   if item in data:
#       data[item] += amount
#  else:
#      data[item] = amount
    # Above it the easy-to-understand version below it the setdefault method
    data[item] = data.setdefault(item,0) + amount


for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

while True:
    # Display a menu of the recipes we know how to cook
    print("Please choose your recipe")
    print("--------------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("checking ingredients...")
        ingredients = recipes[selected_item]
        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            #   if food_item not in pantry:
            #   print(f"\tYou do not have have {food_item}")
            #   This was my way of doing it which was correct
            #   However the instructor did it slightly different, so
            #   We will follow along with his method.
            if required_quantity <= quantity_in_pantry:
                print(f"\t{food_item} OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"\tYou need to buy {quantity_to_buy} of {food_item}")
                # shopping_list[quantity_to_buy] = food_item
                add_to_slist(shopping_list, food_item, quantity_to_buy)
print("This is your Shopping list")

for i in shopping_list.items():
    print(i)
