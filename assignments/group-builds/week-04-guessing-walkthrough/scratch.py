secret = 6
guess = 0
tries = 0
while guess != secret:
    guess = int(input('Guess: '))
    tries += 1
    if guess < secret:
        print('Too low')
    elif guess > secret:
        print('Too high')
print('Correct in', tries, 'tries')
