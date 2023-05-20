# Dice Rolling Simulator
# libraries
import random
import sys
# Dice art by Leodanis Pozo Ramos.
DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}

dice = []
total = 0
while True:
    try:
        num_of_dice = int(input("How many dice do you want to roll [1-10]? "))
        if not num_of_dice:
            print("Please do not leave the input blank")
            continue
        if num_of_dice >= above:
            break
        else:
            print("Please Choose a number")
    except ValueError:
        print("Please Choose a number")


if num_of_dice <= 10:
    print("Please Choose a number from [1-10]")
else:
     sys.exit(1)

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

for line in range(5):
    for die in dice:
        print(DICE_ART.get(die)[line], end="")
    print()

for die in dice:
    total += die
print(f"Total: {total}")
