import random

# Dice faces: brains (B), footsteps (F), shotgun (S)
DICE = {
    'green': ['B', 'B', 'B', 'F', 'F', 'S'],
    'yellow': ['B', 'B', 'F', 'F', 'S', 'S'],
    'red': ['B', 'F', 'F', 'S', 'S', 'S']
}

# Dice pool
dice_cup = ['green'] * 6 + ['yellow'] * 4 + ['red'] * 3

def roll_die(color):
    return random.choice(DICE[color])

def take_turn():
    cup = dice_cup[:]
    random.shuffle(cup)
    brain_count = 0
    shotgun_count = 0
    footsteps = []

    while True:
        # Take 3 dice, replacing footsteps
        hand = footsteps
        while len(hand) < 3 and cup:
            hand.append(cup.pop())
        if not hand:
            break

        print("\nRolling:", hand)
        new_footsteps = []
        for die_color in hand:
            result = roll_die(die_color)
            print(f"{die_color.title()} die shows: {result}")
            if result == 'B':
                brain_count += 1
            elif result == 'S':
                shotgun_count += 1
            else:
                new_footsteps.append(die_color)

        footsteps = new_footsteps
        print(f"Brains: {brain_count}, Shotguns: {shotgun_count}")

        if shotgun_count >= 3:
            print("You got blasted! No brains this turn.")
            return 0

        choice = input("Roll again? (y/n): ").strip().lower()
        if choice != 'y':
            return brain_count

# Main game loop
def play_game():
    print("Welcome to Zombie Dice!")
    score = 0
    while True:
        print(f"\nYour total score: {score}")
        turn_score = take_turn()
        score += turn_score
        print(f"Turn ended with {turn_score} brains.")
        if input("Play another turn? (y/n): ").strip().lower() != 'y':
            break

    print(f"\nFinal score: {score}")

play_game()