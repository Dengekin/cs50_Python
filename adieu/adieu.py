import inflect

names = []
p = inflect.engine()

while True:
    try:
        name = input().strip()
        names.append(name)
    except EOFError:
        break


print(f"Adieu, adieu, to {p.join(names)}")
