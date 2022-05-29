from contents import recipes, pantry




new_repository = {}
for i, g in recipes.items():
    if i == 'Butter chicken':
        new_repository[i] = g
    else:
        print("no")

print(new_repository)



