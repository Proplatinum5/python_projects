
options = "bitcoin", "eth", "dogecoin", "cardino", "amp", "xrp", "0 to leave"

choice = ""

print("hello i would like to inquire some information about you "
               "please select your most liked crypto out of these choices")
for options in options:
    print(options)


for choice in options:


    choice = input("please select a crypto")

    if choice.casefold == "0 to leave":
        print("you have chosen not to participate in the discussion")

    elif choice.casefold() == "bitcoin":
        print("bitcoin is the first biggest crypto to make a big"
              " wave of change in the world how ever there are "
              "environmental concerns with bitcoin so there have"
              " been options coming in place to address that situations")
    elif choice.casefold() == "eth":
        print("Ethereum has been the second biggest lead up into"
              " crypto currency, people say that it may one day "
              "surpass bitcoin which would be quite the feat.")
    elif choice.casefold() == "dogecoin":
        print(" Dogecoin is a huge crypto that was once a meme coin"
              " only created as a joke now it is "
              "being recognized by some of the most influential "
              "people on this earth even"
              " the richest person on the planet elon musk has"
              " acknowledged this coin and heavily supports it "
              "how ever it seems his brother is not following suit")
    elif choice.casefold() == "cardino":
        print("cardino is an exceptionally good crypto tis in the"
              "top ten cryptos and has a promising future")
    elif choice.casefold() == "amp":
        print(" Amp is a unique crypto. it is supposed to be used "
              "as a collateral currency as a means to hlep individuals "
              "feel safe with their exchange of other cryptos it "
              "gets its utilization by being able to transact faster"
              " it seems as though amp may be very valuable in the future")
    elif choice.casefold() == "xrp":
        print("Xrp has been a highly speculated crypto used between cryptos"
              " and was one that was first really globally recognized but "
              "then came under fire from cdertain individuals and got sued"
              " and is being attacked in court however xrp is fighting and "
              "it looks like they may come out on top which would dramatically "
              "increace the value of xrp and bring them back into the crypto"
              " game once again ")
    elif choice == "0":
        print("okay see you next time")

    else:
        print(options)
        #for options in options:
        #   print(options)