# TODO

def luhn_ok (num_str: str) -> bool:
    total = 0
    rev = num_str[::-1]
    for i, ch in enumerate(rev):
        d = int(ch)
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0

def brand(num_str: str) -> str:
    n = len(num_str)
    starts2 = num_str[:2]
    starts1 = num_str[0]

    if n == 15 and starts2 in {"34","37"}:
        return "AMEX"
    if n == 16 and starts2 in {"51","52","53","54","55"}:
        return "MASTERCARD"
    if n in (13,16) and starts1 == "4":
        return "VISA"
    return "INVALID"

def main():
    while True:
        s = input ("Number: ").strip()
        if s.isdigit():
            break

    if luhn_ok(s):
        print(brand(s))
    else:
        print("INVALID")

main()
