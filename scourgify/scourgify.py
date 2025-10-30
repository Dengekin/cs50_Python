import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

pathin = sys.argv[1]
pathout = sys.argv[2]

if not pathin.endswith(".csv") or not pathout.endswith(".csv"):
    sys.exit(1)

try:
    with open(pathin,newline="") as infile, open(pathout, "w",newline="") as outfile:
        reader = csv.DictReader(infile)

        writer = csv.DictWriter(outfile, fieldnames=[ "first", "last", "house"])
        writer.writeheader()

        for row in reader:
            last, first = row["name"].split(", ")
            writer.writerow(
                {
                    "first": first,
                    "last" : last,
                    "house" : row ["house"]
                }
            )
except FileNotFoundError:
    sys.exit(f"Could not read {pathin}")



