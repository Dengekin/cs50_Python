# TODO

while True:
    try:
        owed = float(input("Change owed: "))
        if owed >= 0:
            break
    except ValueError:
        continue

cents = round(owed * 100)

for coin in [25, 10, 5, 3]:
    coins += cents // coin
    cents %= coin

print(coins)
