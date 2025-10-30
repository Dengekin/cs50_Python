
import re
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


main()



"""
“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”

plate_re = re.compile(r'^(?=.{2,6}$)[A-Za-z]{2}[A-Za-z]*([1-9]\d*)?$')
def is_valid(s):
    return bool(plate_re.fullmatch(s))

    """
