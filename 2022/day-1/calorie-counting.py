# --- Libraries --- #

import os
import sys


# --- Functions --- #

def inputs_func():
    # Function to read input.txt file and convert the breakdowns per elf into totals
    inputs = []
    sum = 0

    input_file = open(os.path.join(sys.path[0], "input.txt"), "r")
    for calories in input_file:
        if calories == "\n":
            inputs.append(sum)
            sum = 0
        else:
            sum += int(calories)
    input_file.close()
    return inputs


# --- Main --- #

def main():
    cal_list = []
    cal_list_sums = []

    cal_list = inputs_func()
    cal_list.sort(reverse=True)

    print("Part 1: ", max(cal_list))

    print("\nPart 2:", cal_list[0] + cal_list[1] + cal_list[2])


if __name__ == "__main__":
    main()
