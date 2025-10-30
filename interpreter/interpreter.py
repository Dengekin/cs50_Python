math = input("Expression: ").strip()
parts = math.split(" ",2
                   )
first = float(parts[0])
second = float(parts[2])

match parts[1]:
    case "/":
        print(first/second)
    case "*":
        print(first*second)
    case "-":
        print(first-second)
    case "+":
        print(first+second)


