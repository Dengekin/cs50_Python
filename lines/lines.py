import sys


if len(sys.argv) != 2:
    sys.exit(1)

path = sys.argv[1]
if not path.endswith(".py"):
    sys.exit(1)

try:
    with open(path, "r") as f:
        count = 0
        for line in f:
            s = line.strip()
            if s.startswith("#"):
                continue
            elif s == "":
                continue
            else:
                count += 1
except FileNotFoundError:
    sys.exit(1)
except OSError:
    sys.exit(1)

print(count)
