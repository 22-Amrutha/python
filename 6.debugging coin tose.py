import random

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input().lower()

toss = random.randint(0, 1)  # 0 is tails, 1 is heads
toss_str = 'heads' if toss == 1 else 'tails'

if guess == toss_str:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = ''
    while guess not in ('heads', 'tails'):
        guess = input().lower()
    if guess == toss_str:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

"""Bugs in the original code:
guess is a string, but toss is an integer (0 or 1). Comparing them directly (if toss == guess:) will always be False.
Typo: guesss = input() should be guess = input().
The second comparison still compares string to int.
There’s no handling of invalid input on the second guess.

 Improvements:
 Converts toss from int to string (toss_str) for easier comparison.
Ensures both guesses are validated.
Makes the game robust and clean."""