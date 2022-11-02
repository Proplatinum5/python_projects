naruto = {
    "jutsu": ["Shadow Clone Technique",
              "Rasengan",
              "Nature Transformation",
              "Six Paths Senjutsu"
              "Tailed Beast Transformation"],
    "nature": ["Wind Release",
               "Lightning Release",
               "Earth Release",
               "Water Release",
               "Fire Release",
               "Lava Release",
               "Magnet Release",
               "Boil Release",
               "Yin Release",
               "Yang Release",
               "Yin–Yang Release"],
    "village rank": ["hokage"],
    "info card": ["Naruto is one of the most powerful shinobi. "
                  "He is the leader of the leaf"
                  "village and has great might. Naruto can apply his"
                  "nature release to his main jutsu to create several"
                  "variants."]
}
sauske = {
    "jutsu": ["Shadow Clone Technique",
              "Chidori",
              "Bukijutsu",
              "Nature Transformation",
              "Dojutsu"],
    "nature": [ "Lightning Release",
                "Fire Release",
                "Wind Release",
                "Earth Release",
                "Water Release",
                "Yin Release"],
    "village rank": ["shadow hokage"],
    "info card": ["Sauske was once a missing nin who helped save the world"
                  "from the grasp of evil. Sauske is a revived member of "
                  "the leaf village and helps defend it from threats"
                  "sauske has powerful dojutsu (sharnigan) it helps him "
                  "precieve enemy powers and movemens and comes with "
                  "powerfull abilities. Sauske can apply many natures to "
                  "his jutsu to create more powerful ones"]
}

S_RANK_NINJA = {"naruto": naruto,
                "sauske": sauske}
A_Rank_NINJA = {""}

for ninja in S_RANK_NINJA:
    print(ninja)


