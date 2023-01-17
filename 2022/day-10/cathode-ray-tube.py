# --- Libraries --- #

import os
import sys


# --- Functions --- #

def get_instructions_func():
    # Function to get the tree info from the elves' quadcopter
    instructions = []
    instructions_file = open(os.path.join(sys.path[0], "input.txt"), "r")

    for instruction in instructions_file:
        instructions.append(instruction.replace("\n", "").replace("addx ", ""))
    instructions_file.close()
    return instructions


def print_nicely_func(input):
    # Function to print list info nicely
    for line in input:
        print(line)


def iterate_cycles_func(instructions, end_cycle):
    # Function to go through the cycles
    x_register = 1
    cycle_counter = 0
    signal_strength = 0
    sum_of_signal_strengths = 0

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


def crt_sprites_func(instructions):
    # Function to go through the cycles
    x_register = 1
    cycle_counter = 0
    crt = ""
    crt_output = []

    for instruction in instructions:
        if instruction == "noop":
            if x_register-1 <= cycle_counter <= x_register+1:
                crt += "#"
            else:
                crt += " "
            cycle_counter += 1
            if cycle_counter % 40 == 0:
                cycle_counter = 0
                crt += "split"
        else:
            if x_register-1 <= cycle_counter <= x_register+1:
                crt += "#"
            else:
                crt += " "
            cycle_counter += 1
            if cycle_counter % 40 == 0:
                cycle_counter = 0
                crt += "split"
            if x_register-1 <= cycle_counter <= x_register+1:
                crt += "#"
            else:
                crt += " "
            cycle_counter += 1
            if cycle_counter % 40 == 0:
                cycle_counter = 0
                crt += "split"
            x_register += int(instruction)
    crt_output = crt.split("split")
    return crt_output


# --- Main --- #

def main():
    end_cycle = 220
    instructions = get_instructions_func()
    sum_of_signal_strengths = iterate_cycles_func(instructions, end_cycle)
    crt = crt_sprites_func(instructions)

    print("Part 1: ", sum_of_signal_strengths)
    print("Part 2:")
    print_nicely_func(crt)


if __name__ == "__main__":
    main()
