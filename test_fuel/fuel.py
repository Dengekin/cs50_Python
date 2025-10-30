def main():
    while True:
        try:
            fuel = input("Fraction: ").strip()
            percent = convert(fuel)
            break
        except (ValueError, ZeroDivisionError):
            continue
    print(gauge(percent))


def convert(fraction: str) -> int:
    try:
        x, y = fraction.split("/")
        x, y = int(x), int(y)
    except Exception:
        raise ValueError


    if y == 0:
        raise ZeroDivisionError

    if x < 0 or y < 0 or x > y:
        raise ValueError

    return round((x/y)*100)




def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()

"""
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
"""
