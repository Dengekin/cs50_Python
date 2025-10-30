
"""
vowel = input("Input: ").strip()
omit = ""
for ch in vowel:
    if ch.lower() in "aeiou":
        pass
    else:
        omit += ch
print(omit)
"""

def main():
    vowel = input("Input: ").strip()
    print(shorten(vowel))

def shorten(vowel):
    omit = ""
    for ch in vowel:
        if ch.lower() in "aeiou":
            pass
        else:
            omit += ch
    return omit

if __name__ == "__main__":
    main()
