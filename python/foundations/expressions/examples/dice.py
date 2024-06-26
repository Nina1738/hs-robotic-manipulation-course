import random

NUM_SIDES = 6   # constant

def roll_dice():
    """
    Simulate rolling two dice.
    """
    die_1 = random.randint (0, NUM_SIDES)
    die_2 = random.randint (1, NUM_SIDES)
    
    return die_1 + die_2

def main():
    roll_dice()

if __name__ == '__main__':
    main()
