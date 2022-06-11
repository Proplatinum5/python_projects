numbers = {*""}

print(numbers, type(numbers))

#while len(numbers) < 4:
#    next_value = int(input("Please enter you next value: "))
#    numbers.add(next_value)
#print(numbers)

data = ["blue", "red", "blue", "green", "red", "blue", "white"]

# create a set from the list to remove dups
unique_data = set(data)
print(unique_data)

# create a list of unique colours, keeping the order they appeared.
unique_data = list(dict.fromkeys(data))
print(unique_data)
print()
print(dict.fromkeys(data))

numbers.add("1")
numbers.add("2")
numbers.add("3")

print(numbers)