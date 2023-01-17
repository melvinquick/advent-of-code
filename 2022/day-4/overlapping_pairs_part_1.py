# =========
# LIBRARIES
# =========

import os
import sys


# =========
# FUNCTIONS
# =========

# Function to get the pair info that the elves currently have
def get_pairs_func():
    # Local Variables
    pairs = []

    # Local Main Code
    pairs_file = open(os.path.join(sys.path[0], "input.txt"), "r")
    for pair in pairs_file:
        pairs.append(pair.replace("\n",""))
    pairs_file.close()
    return pairs

# Function to split pairs into their own array indices
def split_pairs_func(passed_pairs):
    # Local Variables
    split_pairs = []
    super_split_pairs = []
    counter = 0

    # Local Main Code
    for pair in passed_pairs:
        split_pairs.append(pair.split(","))

    for pair in split_pairs:
        split_pairs[counter][0]= split_pairs[counter][0].split("-")
        split_pairs[counter][1]= split_pairs[counter][1].split("-")
        # print(split_pairs[counter])
        counter += 1
    return split_pairs

# Function to check if a part of a pair is completely enveloped by the other part
def get_enveloped_count_func(passed_split_pairs):
    # Local Variables
    enveloped_pairs_counter = 0
    counter = 0
    index_0 = 0
    index_1 = 1

    # Local Main Code
    for pair in passed_split_pairs:
        if (int(pair[index_0][index_0]) <= int(pair[index_1][index_0])) & (int(pair[index_0][index_1]) >= int(pair[index_1][index_1])):
            enveloped_pairs_counter += 1
        elif (int(pair[index_1][index_0]) <= int(pair[index_0][index_0])) & (int(pair[index_1][index_1]) >= int(pair[index_0][index_1])):
            enveloped_pairs_counter += 1
        counter += 1
    return enveloped_pairs_counter


# ================
# GLOBAL VARIABLES
# ================

pairs = []
split_pairs = []
enveloped_counter = 0


# ====
# MAIN
# ====

if __name__ == "__main__":
    pairs = get_pairs_func()
    split_pairs = split_pairs_func(pairs)
    enveloped_counter = get_enveloped_count_func(split_pairs)
    print(enveloped_counter)