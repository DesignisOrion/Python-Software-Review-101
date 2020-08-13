# Whats wrong with this example? Why is this not optimal.


guess = 1

while True:
    num = input("Please guess the number (between 0-100): ")
    try:
        num = int(num)
    except:
        print("Invalid number, please guess again.")
        continue

    if num < 45:
        print("Your guess was under.")
    elif num > 45:
        print("Your guess was over.")
    else:
        break

    guess += 1

    print(f"You guessed it in {guess} guesses")


# issue 1: 45 is hardcoded and the number should be constant.
# issue 2: the number is entered is pass the range of 0 - 100.
# issue 3: What if you wanted to use the program multiple times, you would have to go into the program and change each line of code to fit the needs.
