# =========
# LIBRARIES
# =========

import os
import sys


# =========
# FUNCTIONS
# =========

# This function reads in the strategy file and removes the "\n" from each line
def get_strategy_inputs_func():
    # Local Variables
    strategy_inputs = []

    # Local Main Code
    strategy_input_file = open(os.path.join(sys.path[0], "input.txt"), "r")
    for strategy in strategy_input_file:
        strategy_inputs.append(strategy.replace("\n",""))
    return strategy_inputs

# This function takes the previously read in strategy file and calculates your total score
def get_total_score_func(local_strategy_array):
    # Local Variables
    score_sum = 0
    strategies = local_strategy_array
    # Local Main Code
    for strategy in strategies:
        match strategy:
            case "A X":
                score_sum += 3
            case "A Y":
                score_sum += 4
            case "A Z":
                score_sum += 8
            case "B X":
                score_sum += 1
            case "B Y":
                score_sum += 5
            case "B Z":
                score_sum += 9
            case "C X":
                score_sum += 2
            case "C Y":
                score_sum += 6
            case "C Z":
                score_sum += 7
            case _:
                print("Not a valid outcome")

    return score_sum


# ================
# GLOBAL VARIABLES
# ================

strategy_array = []
total_score = 0

# ====
# MAIN
# ====


if __name__ == "__main__":
    strategy_array = get_strategy_inputs_func()
    total_score = get_total_score_func(strategy_array)
    print(total_score)
