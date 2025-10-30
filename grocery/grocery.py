shoplist = {}

while True:
    try:
        item = input().strip().upper()
        shoplist[item] = shoplist.get(item,0) + 1
    except EOFError:
        break
for item in sorted(shoplist):
    print(f"{shoplist[item]} {item}")
