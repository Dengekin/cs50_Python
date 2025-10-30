# TODO
while True:
    try:
        hei = int(input("Height: "))
        if hei in range(1,9):
            break
    except ValueError:
        continue


for line in range(1, hei+1):
    print(" " * (hei-line), end="")
    print("#" * line,end="")
    print(" " * 2, end="")
    print("#" * line)

