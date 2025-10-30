while True:
    try:
        fuel = input("Fraction: ").strip()
        x, y = fuel.split("/")
        x, y = int(x), int(y)
        if y == 0 or x > y:
            raise ValueError
        percent = round((x/y)*100)
        break
    except (ValueError, ZeroDivisionError):
        continue
if percent <= 1:
    print("E")
elif percent >= 99:
    print("F")
else:
    print(f"{percent}%")
