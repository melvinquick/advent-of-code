# =========
# LIBRARIES
# =========

import os
import sys

# =========
# FUNCTIONS
# =========

# Function to get the tree info from the elves' quadcopter
def get_trees_func():
    # Local Variables
    trees = []
    individual_trees = []

    # Local Main Code
    trees_file = open(os.path.join(sys.path[0], "input.txt"), "r")
    for tree in trees_file:
        trees.append(tree.replace("\n", ""))
    trees_file.close()
    return trees

# Function to get nice printing of multi-dimensional list
def print_nicely_func(input):
    # Local Variables / Local Main Code
    for line in input:
        print(line)

# Function to check if tree is visible from any direction
def visible(trees):
    # Local Variable
    counter = 1

    # Local Main Code
    while counter <= len(trees)-1:
        if trees[0] <= trees[counter]:
            return False
        counter += 1
    return True

# Function to get the visibility of each tree
def get_tree_visibility_func(trees):
    # Local Variable
    visible_count_edge = 0
    visible_count_interior = 0
    trees_across = len(trees[0])-1
    trees_down = len(trees)-1
    tree = []
    top_check = False
    bottom_check = False
    left_check = False
    right_check = False
    counter_1 = 0
    counter_2 = 0
    surrounding_counter = 0

    # Local Main Code
    while counter_1 <= trees_down:
        counter_2 = 0
        while counter_2 <= trees_across:
            # Get Edge Trees
            if counter_1 == 0 or counter_1 == trees_down or counter_2 == 0 or counter_2 == trees_across:
                visible_count_edge += 1
            else:
                # Get Top Surrounding trees
                surrounding_counter = 0
                tree = []
                while surrounding_counter <= counter_1:
                    tree.append(trees[surrounding_counter][counter_2])
                    surrounding_counter += 1
                tree.reverse()
                top_check = visible(tree)

                # Get Bottom Surrounding Trees
                surrounding_counter = counter_1
                tree = []
                while surrounding_counter <= trees_down:
                    tree.append(trees[surrounding_counter][counter_2])
                    surrounding_counter += 1
                bottom_check = visible(tree)

                # Get Left Surrounding Trees
                surrounding_counter = 0
                tree = []
                while surrounding_counter <= counter_2:
                    tree.append(trees[counter_1][surrounding_counter])
                    surrounding_counter += 1
                tree.reverse()
                left_check = visible(tree)

                # Get Right Surrounding Trees
                surrounding_counter = counter_2
                tree = []
                while surrounding_counter <= trees_across:
                    tree.append(trees[counter_1][surrounding_counter])
                    surrounding_counter += 1
                right_check = visible(tree)

                if top_check or bottom_check or left_check or right_check:
                    visible_count_interior += 1

            counter_2 += 1
        counter_1 += 1
    # print(visible_count_edge)
    # print(visible_count_interior)
    return visible_count_edge+visible_count_interior


# ================
# GLOBAL VARIABLES
# ================

trees = []
visible_count = 0


# ====
# MAIN
# ====

if __name__ == "__main__":
    trees = get_trees_func()
    visible_count = get_tree_visibility_func(trees)
    print(visible_count)
