# --- Libraries --- #

import os
import sys

# --- Functions --- #


def get_crates_and_moves_func():
    # Function to get the crate info that the elves currently have
    crates_and_moves = []
    crates_file = open(os.path.join(sys.path[0], "input.txt"), "r")

    for crate in crates_file:
        crates_and_moves.append(crate.replace("\n", ""))
    crates_file.close()
    return crates_and_moves


def get_moves_func(passed_crates_and_moves):
    # Function to get just the moves from the input
    moves_1 = []
    moves_2 = []

    for line in passed_crates_and_moves:
        if "move" in line:
            moves_1.append(line)
    for line in moves_1:
        moves_2.append(line.strip("move ").replace(
            "from ", "").replace("to ", "").split())
    return moves_2


def get_crates_func(passed_crates_and_moves):
    # Function to get just the crates from the input
    crates = []

    for line in passed_crates_and_moves:
        if "move" in line:
            continue
        else:
            crates.append(line)
    crates.pop()
    return crates


def remove_extra_crate_chars_func(passed_crates):
    # Function to remove extra characters from crates
    lines = []
    chars = []

    for line in passed_crates:
        chars = []
        for char in line:
            if char == "[" or char == "]":
                chars.append(" ")
            else:
                chars.append(char)
        lines.append(chars)
    return lines


def correct_crate_columns(passed_crates):
    # Function to get crates into correct columns
    crates_1 = []
    crates_2 = []
    crates_3 = []
    crates_4 = []
    crates_5 = []
    chars = []

    for char in range(len(passed_crates[0])):
        crates_2 = []
        for line in passed_crates:
            crates_2.append(line[char])
        crates_1.append(crates_2)
    for line in crates_1:
        crates_3.append(line[::-1])
    for line in crates_3:
        if line[0] == " ":
            continue
        else:
            crates_4.append(line)
    for line in crates_4:
        chars = []
        for char in line:
            if char != " ":
                chars.append(char)
        crates_5.append(chars)
    return crates_5


def do_moves_part_1(passed_crates, passed_moves):
    # Function to do moves from input
    top_crates = []
    counter_1 = 0
    counter_2 = 0

    for move in passed_moves:
        counter_1 = int(move[0])-1
        while counter_1 >= 0:
            passed_crates[int(move[2]) -
                          1].append(passed_crates[int(move[1])-1].pop())
            counter_1 -= 1
    while counter_2 <= (len(passed_crates)-1):
        top_crates.append(passed_crates[counter_2][-1])
        counter_2 += 1
    return top_crates


def do_moves_part_2(passed_crates, passed_moves):
    # Function to do moves from input but for part 2
    top_crates = []
    temp_list = []
    temp_counter = 0
    counter_1 = 0
    counter_2 = 0

    for move in passed_moves:
        counter_1 = int(move[0])-1
        temp_list = []
        while counter_1 >= 0:
            temp_list.append(passed_crates[int(move[1])-1].pop())
            counter_1 -= 1
        temp_counter = len(temp_list)-1
        while temp_counter >= 0:
            passed_crates[int(move[2])-1].append(temp_list.pop())
            temp_counter -= 1
    while counter_2 <= (len(passed_crates)-1):
        top_crates.append(passed_crates[counter_2][-1])
        counter_2 += 1
    return top_crates


# --- Main --- #

def main():
    crates_and_moves = get_crates_and_moves_func()
    moves = get_moves_func(crates_and_moves)
    crates = get_crates_func(crates_and_moves)
    crates = remove_extra_crate_chars_func(crates)
    crates = correct_crate_columns(crates)
    top_crates = do_moves_part_1(crates, moves)

    print("Part 1: ", top_crates)

    crates_and_moves = get_crates_and_moves_func()
    moves = get_moves_func(crates_and_moves)
    crates = get_crates_func(crates_and_moves)
    crates = remove_extra_crate_chars_func(crates)
    crates = correct_crate_columns(crates)
    top_crates = do_moves_part_2(crates, moves)

    print("Part 2: ", top_crates)


if __name__ == "__main__":
    main()
