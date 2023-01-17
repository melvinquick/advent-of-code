# =========
# LIBRARIES
# =========

import os
import sys


# =========
# FUNCTIONS
# =========

# Function to get the rucksack storage info that the elf currently has
def get_rucksacks_func():
    # Local Variables
    rucksacks = []

    # Local Main Code
    rucksack_file = open(os.path.join(sys.path[0], "input.txt"), "r")
    for rucksack in rucksack_file:
        rucksacks.append(rucksack.replace("\n",""))
    rucksack_file.close()
    return rucksacks

# Function to get the priority of an item
def get_item_priority_func(passed_matches):
    # Local Variables
    priority_of_item = 0
    priority_item_sum = 0

    # Local Main Code
    for match in passed_matches:
        match match:
            case "a":
                priority_of_item = 1
            case "b":
                priority_of_item = 2
            case "c":
                priority_of_item = 3
            case "d":
                priority_of_item = 4
            case "e":
                priority_of_item = 5
            case "f":
                priority_of_item = 6
            case "g":
                priority_of_item = 7
            case "h":
                priority_of_item = 8
            case "i":
                priority_of_item = 9
            case "j":
                priority_of_item = 10
            case "k":
                priority_of_item = 11
            case "l":
                priority_of_item = 12
            case "m":
                priority_of_item = 13
            case "n":
                priority_of_item = 14
            case "o":
                priority_of_item = 15
            case "p":
                priority_of_item = 16
            case "q":
                priority_of_item = 17
            case "r":
                priority_of_item = 18
            case "s":
                priority_of_item = 19
            case "t":
                priority_of_item = 20
            case "u":
                priority_of_item = 21
            case "v":
                priority_of_item = 22
            case "w":
                priority_of_item = 23
            case "x":
                priority_of_item = 24
            case "y":
                priority_of_item = 25
            case "z":
                priority_of_item = 26
            case "A":
                priority_of_item = 27
            case "B":
                priority_of_item = 28
            case "C":
                priority_of_item = 29
            case "D":
                priority_of_item = 30
            case "E":
                priority_of_item = 31
            case "F":
                priority_of_item = 32
            case "G":
                priority_of_item = 33
            case "H":
                priority_of_item = 34
            case "I":
                priority_of_item = 35
            case "J":
                priority_of_item = 36
            case "K":
                priority_of_item = 37
            case "L":
                priority_of_item = 38
            case "M":
                priority_of_item = 39
            case "N":
                priority_of_item = 40
            case "O":
                priority_of_item = 41
            case "P":
                priority_of_item = 42
            case "Q":
                priority_of_item = 43
            case "R":
                priority_of_item = 44
            case "S":
                priority_of_item = 45
            case "T":
                priority_of_item = 46
            case "U":
                priority_of_item = 47
            case "V":
                priority_of_item = 48
            case "W":
                priority_of_item = 49
            case "X":
                priority_of_item = 50
            case "Y":
                priority_of_item = 51
            case "Z":
                priority_of_item = 52
        priority_item_sum += priority_of_item
    
    return priority_item_sum

# Function to get which item appears in both compartments of each rucksack
def get_item_that_appears_in_each_compartment_func(passed_rucksacks):
    # Local Variables
    item_count = 0
    counter = 0
    halfway = 0
    compartment_1 = []
    compartment_2 = []
    matching_items = []

    # Local Main Code 
    for rucksack in passed_rucksacks:
        item_count = len(rucksack)
        halfway = int((item_count/2))
        compartment_1 = rucksack[:halfway]
        compartment_2 = rucksack[halfway:]
        for item in compartment_1:
            if item in compartment_2:
                matching_items.append(item)
                break
    return matching_items
        

# ================
# GLOBAL VARIABLES
# ================

rucksacks = []
compartment_matches = []
priority_sum = 0


# ====
# MAIN
# ====

if __name__ == "__main__":
    rucksacks = get_rucksacks_func()
    compartment_matches = get_item_that_appears_in_each_compartment_func(rucksacks)
    priority_sum = get_item_priority_func(compartment_matches)
    print(priority_sum)