def main():
    time_str = input("What time is it? ").strip()
    saat = convert(time_str)

    if 7 <= saat <= 8:
        print("breakfast time")
    elif 12 <= saat <= 13:
        print("lunch time")
    elif 18 <= saat <= 19:
        print("dinner time")

def convert(time):
    parts = time.split(":")
    hours = float(parts[0])
    minutes = float(parts[1])
    return hours + minutes / 60

if __name__ == "__main__":
    main()




"""
Meal Time
breakfast between 7:00 and 8:00,
lunch between 12:00 and 13:00, and
dinner between 18:00 and 19:00.

#:## or ##:##.
#:## a.m. and ##:## a.m.
#:## p.m. and ##:## p.m.
For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

convert is a function that converts time, a str in 24-hour format,
to the corresponding number of hours as a float.
For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes),
convert should return 7.5 (i.e., 7.5 hours).

"""
