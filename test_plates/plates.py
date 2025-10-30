def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    #uzunluk
    if not (2 <= len(s) <= 6):
        return False

    #sadece
    if not s.isalnum():
        return False

    #lik iki karakter harf
    if not s[:2].isalpha():
        return False

    # Rakam
    for i,ch in enumerate(s):
        if ch.isdigit():
            if ch == '0':
                return False
            return s[i:].isdigit()

    return True

if __name__ == "__main__":
    main()



