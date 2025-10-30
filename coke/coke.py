coke = 50
while coke != 0:
    print(f"Amount Due: {coke}")
    coin = int(input("Insert Coin: "))
    if coin in [25, 10, 5]:
        coke -= coin
    else:
        continue


print(f"Change Owed: {-coke}")
