# Dice Rolling Simulator

# libraries
from tkinter import *
from random import randint
import sys

# User Input
num_dice_input = input("How many dice do you want to roll? [1-6]")
num_dice = parse_input(num_dice_input)
# Defining Functions
def parse_input(input_string):
    if input_string.string() in {"1", "2", "3", "4", "5", "6"}:
        return int(input_string)
    else:
        print("Please choose a number from 1 to 6.")
        raise sys.exit(1)


