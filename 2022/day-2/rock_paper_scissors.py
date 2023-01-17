# --- Libraries --- #

import os
import sys


# --- Functions --- #

def get_strategy_inputs_func():
    # This function reads in the strategy file and removes the "\n" from each line
    strategy_inputs = []

    strategy_input_file = open(os.path.join(sys.path[0], "input.txt"), "r")
    for strategy in strategy_input_file:
        strategy_inputs.append(strategy.replace("\n", ""))
    strategy_input_file.close()
    return strategy_inputs


def part_1_score_func(local_strategy_array):
    # This function takes the previously read in strategy file and calculates your total score
    score_sum = 0
    strategies = local_strategy_array

    for strategy in strategies:
        match strategy:
            case "A X":
                score_sum += 4
            case "A Y":
                score_sum += 8
            case "A Z":
                score_sum += 3
            case "B X":
                score_sum += 1
            case "B Y":
                score_sum += 5
            case "B Z":
                score_sum += 9
            case "C X":
                score_sum += 7
            case "C Y":
                score_sum += 2
            case "C Z":
                score_sum += 6
            case _:
                print("Not a valid outcome")
    return score_sum

def part_2_score_func(local_strategy_array):
    # This function takes the previously read in strategy file and calculates your total score
    score_sum = 0
    strategies = local_strategy_array

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


# --- Main --- #

def main():
    strategy_array = []
    total_score = 0

    strategy_array = get_strategy_inputs_func()

    total_score = part_1_score_func(strategy_array)
    print("Part 1: ", total_score)

    total_score = part_2_score_func(strategy_array)
    print("Part 2: ", total_score)

if __name__ == "__main__":
    main()
