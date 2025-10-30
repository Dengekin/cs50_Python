def main():
    print(convert(input()))

def convert(text):
    text = text.replace(":)","🙂")
    text = text.replace(":(","🙁")
    return text

main()
