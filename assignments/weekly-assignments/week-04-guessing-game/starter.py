secret = 5
guess = 0
tries = 0

while guess != secret:
    guess = int(input("Guess a number from 1 to 10: "))
    tries += 1
    if guess < secret:
        print("Too low.")
    elif guess > secret:
        print("Too high.")
    else:
        print("Correct.")

print("Tries:", tries)
