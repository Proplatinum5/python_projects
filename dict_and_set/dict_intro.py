vehicles = {
    'dream': 'Honda 250T',
    'er5': 'kawaskai ER5',
    'can-am': 'Bombardier Can_Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiest Ghia 1.4',
    'roadster': 'Triumph Street Triple'
}

vehicles["starfighter"] = "Lockhead-F104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["Toy"] = "glider"

#upgrade the virago
vehicles["virago"] = "Yamaha XV535"

del vehicles["starfighter"]
#del vehicles["F1"]
result = vehicles.pop("f1", None)
print(result)
plane = vehicles.pop("learjet")
print(plane)

bike = vehicles.pop("hotrod", "not present")
print(bike)
print()
#for key in vehicles:
#   print(key, vehicles[key], sep=", ")
# writing a code like this is slower and less effective

for key, value in vehicles.items():
    print(key, value, sep=", ")


