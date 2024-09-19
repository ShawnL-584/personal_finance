import random

secret = random.randint(1, 100)
print(secret)
min_value = 1
max_value = 100

while True:
    guess = input(
        f"Guess your number(the range is {min_value} to {max_value}): ")
    if int(guess) < min_value or int(guess) > max_value:
        print('Your guess is out the the range.')
        continue
    if int(guess) == secret:
        print(f'The secret is {secret}.')
        break
    elif int(guess) < secret:
        min_value = int(guess)
    elif int(guess) > secret:
        max_value = int(guess)
