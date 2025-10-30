import random

def get_level():
    while True:
        try:
            lvl = int(input("Level: ").strip())
            if lvl in(1, 2, 3):
                return lvl
        except ValueError:
            pass

def gen_operand(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)

def gen_question(level, ops):
    op = random.choice(ops)
    x = gen_operand(level)
    y = gen_operand(level)

    if op == '+':
        ans = x + y
    elif op == '-':
        # Negatif sonuç olmasın istiyorsan x >= y yap
        if x < y:
            x, y = y, x
        ans = x - y
    elif op == '*':
        ans = x * y
    elif op == '/':
        # Bölme için: 0'a bölmeyi ve ondalığı önlemek adına y'yi 1..9 seç,
        # x'i de y'nin katı yapalım ki sonuç tam sayı olsun.
        y = random.randint(1, 9)
        k = gen_operand(level) // max(1, y)
        if k == 0:
            k = random.randint(1, 9)
        x = y * k
        ans = x // y
        op = '÷'  # ekranda daha hoş dursun; istersen '/' bırak
    else:
        # Güvenlik için
        op = '+'
        ans = x + y

    return x, op, y, ans


def main():
    level = get_level()
    score = 0
    OPS = ['+']

    for _ in range(10):
        x, op, y, answer = gen_question(level,OPS)
        tries = 0
        solved = False

        while tries < 3:
            try:
                user_in = input(f"{x} {op} {y} = ").strip()
                user = int(user_in)
            except ValueError:
                print("EEE")
                tries += 1
                continue

            if user == answer:
                score += 1
                solved = True
                break
            else:
                print("EEE")
                tries += 1

        if not solved:
            print(f"{x} {op} {y} = {answer}")

    print(f"Score: {score}")

if __name__ == "__main__":
    main()










"""
while True:
   level = input("Level: ").strip()
   if int(level) in [1, 2, 3]:
       break
   else:
      continue

for _ in range(10):
   x = random.randint(0, 9)
   y = random.randint(0, 9)
   z = random.choice(["+","/","*","-"])
   questions.append({"x": x,"y": y,"z": z})

index = 0
while index < 10:
    user_answer = input(f"{questions[index]["x"]} {questions[index]["z"]} {questions[index]["y"]} =")
    user_answer = int(user_answer)
    match questions[index]["z"]:
       case "+":
           answer = questions[index]["x"] + questions[index]["y"]
       case "-":
           answer = questions[index]["x"] - questions[index]["y"]
       case "/":
           answer = questions[index]["x"] / questions[index]["y"]
       case "*":
           answer = questions[index]["x"] * questions[index]["y"]
    false_count = 0
    while false_count < 3
    if not answer == user_answer:
       false_count += 1
       continue
    elif answer == user_answer:
       return break
    index += 1

"""
