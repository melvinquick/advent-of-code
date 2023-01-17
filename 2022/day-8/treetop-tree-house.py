# --- Libraries --- #

import os
import sys


# --- Functions --- #

def get_trees_func():
    # Function to get the tree info from the elves' quadcopter
    trees = []
    individual_trees = []

    trees_file = open(os.path.join(sys.path[0], "input.txt"), "r")
    for tree in trees_file:
        trees.append(tree.replace("\n", ""))
    trees_file.close()
    return trees


def visible(trees):
    # Function to check if tree is visible from any direction
    counter = 1

    while counter <= len(trees)-1:
        if trees[0] <= trees[counter]:
            return False
        counter += 1
    return True


def scenic_score_func(trees):
    # Function to get the scenic score of a tree
    counter = 1
    scenic_score = 0

    while counter <= len(trees)-1:
        if trees[0] > trees[counter]:
            scenic_score += 1
        if trees[0] <= trees[counter]:
            scenic_score += 1
            break
        counter += 1
    return scenic_score


def get_tree_visibility_func(trees):
    # Function to get the visibility of each tree
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
    return visible_count_edge+visible_count_interior


def get_best_scenic_score_func(trees):
    # Function to get the best scenic score of all trees
    trees_across = len(trees[0])-1
    trees_down = len(trees)-1
    tree = []
    top_check = 0
    bottom_check = 0
    left_check = 0
    right_check = 0
    counter_1 = 0
    counter_2 = 0
    surrounding_counter = 0
    scenic_score = []

    while counter_1 <= trees_down:
        counter_2 = 0
        while counter_2 <= trees_across:
            # Get Edge Trees
            if counter_1 == 0 or counter_1 == trees_down or counter_2 == 0 or counter_2 == trees_across:
                counter_2 += 1
                continue
            else:
                # Get Top Surrounding trees
                surrounding_counter = 0
                tree = []
                while surrounding_counter <= counter_1:
                    tree.append(trees[surrounding_counter][counter_2])
                    surrounding_counter += 1
                tree.reverse()
                top_check = scenic_score_func(tree)

                # Get Bottom Surrounding Trees
                surrounding_counter = counter_1
                tree = []
                while surrounding_counter <= trees_down:
                    tree.append(trees[surrounding_counter][counter_2])
                    surrounding_counter += 1
                bottom_check = scenic_score_func(tree)

                # Get Left Surrounding Trees
                surrounding_counter = 0
                tree = []
                while surrounding_counter <= counter_2:
                    tree.append(trees[counter_1][surrounding_counter])
                    surrounding_counter += 1
                tree.reverse()
                left_check = scenic_score_func(tree)

                # Get Right Surrounding Trees
                surrounding_counter = counter_2
                tree = []
                while surrounding_counter <= trees_across:
                    tree.append(trees[counter_1][surrounding_counter])
                    surrounding_counter += 1
                right_check = scenic_score_func(tree)

                scenic_score.append(
                    top_check * bottom_check * left_check * right_check)

            counter_2 += 1
        counter_1 += 1
    return max(scenic_score)


# --- Main --- #

def main():
    trees = get_trees_func()
    visible_count = get_tree_visibility_func(trees)
    best_scenic_score = get_best_scenic_score_func(trees)

    print("Part 1: ", visible_count)
    print("Part 2: ", best_scenic_score)


if __name__ == "__main__":
    main()
