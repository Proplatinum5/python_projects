naruto_characters = [{"naruto"},{"sauske"},{"sakura"},
                     {"choji"}, {"ino"}, {"shikamaru"},
                     {"minato"}, {"jirah"}, {"kakashi"},
                     {"hogoromo"}, {"madara"}]

rasengan_users = [{"naruto"}, {"minato"},
                  {"jirah"}, {"kakashi"}]

chidori_users = [{"kakashi"}, {"sauske"}]


print("For this mission we need to have ninja that know rasengan and chidori for "
      "maximum effectiveness")

this_mission = set()

for user in rasengan_users:
    this_mission |= user

for user in chidori_users:
    this_mission |= user

print(this_mission)

