# =========
# LIBRARIES
# =========

import os
import sys

# =========
# FUNCTIONS
# =========

# Function to get the tree info from the elves' quadcopter
def get_instructions_func():
    # Local Variables
    instructions = []

    # Local Main Code
    instructions_file = open(os.path.join(sys.path[0], "input.txt"), "r")
    for instruction in instructions_file:
        instructions.append(instruction.replace("\n", "").replace("addx ", ""))
    instructions_file.close()
    return instructions

# Function to print list info nicely
def print_nicely_func(input):
    # Local Variables / Local Main Code
    for line in input:
        print(line)

# Function to go through the cycles
def iterate_cycles_func(instructions, end_cycle):
    # Local Variable
    x_register = 1
    cycle_counter = 0
    signal_strength = 0
    sum_of_signal_strengths = 0

    # Local Main Code
    for instruction in instructions:
        signal_strength = 0
        if cycle_counter <= end_cycle:
            if instruction == "noop":
                cycle_counter += 1
                if cycle_counter % 40 == 20:
                    signal_strength = x_register * cycle_counter
            else:
                cycle_counter += 1
                if cycle_counter % 40 == 20:
                    signal_strength = x_register * cycle_counter
                cycle_counter += 1
                if cycle_counter % 40 == 20:
                    signal_strength = x_register * cycle_counter
                x_register += int(instruction)

            sum_of_signal_strengths += signal_strength
    
    return sum_of_signal_strengths


# ================
# GLOBAL VARIABLES
# ================

instructions = []
end_cycle = 220
sum_of_signal_strengths = 0


# ====
# MAIN
# ====

if __name__ == "__main__":
    instructions = get_instructions_func()
    sum_of_signal_strengths = iterate_cycles_func(instructions, end_cycle)
    print(sum_of_signal_strengths)
