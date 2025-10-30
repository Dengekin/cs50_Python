"""
answer = input("Greeting: ").strip()
if answer.split()[0].strip(",.!?").lower() == "hello":
    print("$0")
elif answer.split()[0][0].lower() == "h":
    print("$20")
else:
    print("$100")
"""

def main():
    answer = input("Greeting: ").strip()
    print(value(answer))



def value(greeting):
    if greeting.split()[0].strip(",.!?").lower() == "hello":
        return "$0"
    elif greeting.split()[0][0].lower() == "h":
        return "$20"
    else:
        return "$100"



if __name__ == "__main__":
    main()
