# --- Libraries --- #

import os
import sys


# --- Functions --- #

def get_pairs_func():
    # Function to get the pair info that the elves currently have
    pairs = []

    pairs_file = open(os.path.join(sys.path[0], "input.txt"), "r")
    for pair in pairs_file:
        pairs.append(pair.replace("\n",""))
    pairs_file.close()
    return pairs

def split_pairs_func(passed_pairs):
    # Function to split pairs into their own array indices
    split_pairs = []
    super_split_pairs = []
    counter = 0

    for pair in passed_pairs:
        split_pairs.append(pair.split(","))

    for pair in split_pairs:
        split_pairs[counter][0]= split_pairs[counter][0].split("-")
        split_pairs[counter][1]= split_pairs[counter][1].split("-")
        counter += 1
    return split_pairs

def get_enveloped_count_func(passed_split_pairs):
    # Function to check if a part of a pair is completely enveloped by the other part
    enveloped_pairs_counter = 0
    counter = 0
    index_0 = 0
    index_1 = 1

    for pair in passed_split_pairs:
        if (int(pair[index_0][index_0]) <= int(pair[index_1][index_0])) & (int(pair[index_0][index_1]) >= int(pair[index_1][index_1])):
            enveloped_pairs_counter += 1
        elif (int(pair[index_1][index_0]) <= int(pair[index_0][index_0])) & (int(pair[index_1][index_1]) >= int(pair[index_0][index_1])):
            enveloped_pairs_counter += 1
        counter += 1
    return enveloped_pairs_counter

def get_overlapped_count_func(passed_split_pairs):
    # Function to check pairs are overlapping at all
    overlapped_pairs_counter = 0
    counter = 0
    index_0 = 0
    index_1 = 1

    for pair in passed_split_pairs:
        if (int(pair[index_0][index_0]) >= int(pair[index_1][index_0])) & (int(pair[index_0][index_0]) <= int(pair[index_1][index_1])):
            overlapped_pairs_counter += 1
        elif (int(pair[index_0][index_1]) >= int(pair[index_1][index_0])) & (int(pair[index_0][index_1]) <= int(pair[index_1][index_1])):
            overlapped_pairs_counter += 1
        elif (int(pair[index_1][index_0]) >= int(pair[index_0][index_0])) & (int(pair[index_1][index_0]) <= int(pair[index_0][index_1])):
            overlapped_pairs_counter += 1
        elif (int(pair[index_1][index_1]) >= int(pair[index_0][index_0])) & (int(pair[index_1][index_1]) <= int(pair[index_0][index_1])):
            overlapped_pairs_counter += 1
        counter += 1
    return overlapped_pairs_counter


# --- Main --- #

def main():
    pairs = get_pairs_func()
    split_pairs = split_pairs_func(pairs)
    enveloped_counter = get_enveloped_count_func(split_pairs)
    overlapped_counter = get_overlapped_count_func(split_pairs)

    print("Part 1: ", enveloped_counter)
    print("Part 2: ", overlapped_counter)

if __name__ == "__main__":
    main()