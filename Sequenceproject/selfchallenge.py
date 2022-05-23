cryptos = [["btc", "eth", "doge"],
           ["btc", "poka", "doge"],
           ["btc", "amp", "eth", "doge"],
           ["amp", "eth", "blinu", "doge"]]

for coins in cryptos:
    for index in range(len(coins) - 1, -1, -1):
        if coins[index] == "doge":
            del coins[index]
    print(coins)