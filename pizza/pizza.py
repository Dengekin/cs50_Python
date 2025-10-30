import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

path = sys.argv[1]

if not path.endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    with open(path, newline="") as file:
        reader = csv.reader(file)  # reader = csv.DictReader(file)
        table = list(reader)       # header = reader.fieldnames
        header = table[0]          # rows = [list(row.values()) for row in reader] # Dict --> List
        rows = table[1:]

    print(tabulate(rows, headers=header, tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")



