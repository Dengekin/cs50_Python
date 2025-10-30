# TODO
def main():
    text = input("Text: ")

    letters = sum(ch.isalpha() for ch in text)
    words = len(text.split())
    sentences = sum(ch in ".!?" for ch in text)

    if words == 0:
        print("Before Grade 1")
        return

    L = letters / words *100
    S = sentences / words *100
    index = 0.0588 * L - 0.296 * S - 15.8
    grade = round(index)

    if grade < 1:
        print("Before Grade 1")
    elif grade >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {grade}")

main()
