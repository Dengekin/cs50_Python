month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date = input("Date: ").strip()

        if "/" in date:
            mon, day, year = date.split("/")
            mon, day, year = int(mon), int(day), int(year)
            if not (1 <= mon <= 12 and 1 <= day <= 31):
                continue
            print(f"{year:04}-{mon:02}-{day:02}")
            break

        elif "," in date:
            mon, day, year = date.replace(",", "").split()
            if mon in month:
                mont = month.index(mon) + 1
                day, year = int(day), int(year)
                if not (1 <= mont <= 12 and 1 <= day <= 31):
                    continue
                print(f"{year:04}-{mont:02}-{day:02}")
                break

    except ValueError:
        continue

