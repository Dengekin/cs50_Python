import random

while True:
    level_input = input("Level: ").strip()
    if level_input.isdigit() and int(level_input) > 0:
        level_input = int(level_input)
        break
    else:
        continue

n = random.randint(1,level_input)
#n = random.randrange(1, level_input + 1) 

while True:
    guess = input("Guess: ").strip()
    if not (guess.isdigit() and int(guess) > 0):
        continue
    guess = int(guess)
    if guess < n:
        print("Too small!")
        continue
    elif guess > n:
        print("Too large!")
        continue
    elif guess == n:
        print("Just right!")
        break


