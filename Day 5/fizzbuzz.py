for number in range(1, 101):
    output = "Fizz" if number % 3 == 0 else ""
    output += "Buzz" if number % 5 == 0 else ""
    print(output or number) 