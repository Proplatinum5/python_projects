from contents import recipes
def copy_fun(data: dict) -> dict:
    """copy a dictionary given a parameter and return a simple deep
    copy of the original dictionary"""
    data_2 = {}
    for key, value in data.items():
        new_value = value.copy()
        data_2[key] = new_value
    return data_2



nature = {
    "plants": ["flower", "tree", "fruit"],
    "animals": ["lions", "tigers", "bears"],
    "land form": ["moutains", "rivers", "valley"]
}
#print("this is nature the original list")
#print(nature)
#print()
#print("This is the copied list of nature using my def function ")
#print(copy_fun(nature))

recipes_copy = copy_fun(recipes)
recipes_copy["Butter chicken"]["ginger"] = 300
print(id(recipes_copy["Butter chicken"]["ginger"]))
print(id(recipes["Butter chicken"]["ginger"]))
print(recipes["Butter chicken"])
print(recipes_copy["Butter chicken"])

