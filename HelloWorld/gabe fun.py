shp = 100
atk = 10
heal = 10
mhp = 50
matk = 5
while mhp > 0:
    txt = input("Attack or Heal").lower()
    if txt == "attack":
        mhp = mhp - atk
        hp = hp - matk
        print("The monster's health is: " + str(mhp))
        print("Your HP is: " + str(hp))
    elif txt == "heal":
        hp = hp + heal
        hp = hp - matk
        print("The monster's health is: " + str(mhp))
        print("Your HP is: " + str(hp))
    else:
        print("I SAID ATTACK OR HEAL")
if mhp <= 0:
    print("YOU WIN")
