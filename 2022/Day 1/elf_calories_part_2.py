# =========
# LIBRARIES
# =========

import os
import sys


# =========
# FUNCTIONS
# =========

# Function to read input.txt file and convert the breakdowns per elf into totals
def get_calorie_inputs_func():
    # Local Variables
    calorie_inputs = []
    calorie_sums_per_elf = 0

    # Local Main Code
    calorie_input_file = open(os.path.join(sys.path[0], "input.txt"), "r")
    for calories in calorie_input_file:
        if calories == "\n":
            calorie_inputs.append(calorie_sums_per_elf)
            calorie_sums_per_elf = 0
        else:
            calorie_sums_per_elf += int(calories)
    calorie_input_file.close()
    return calorie_inputs


# ================
# GLOBAL VARIABLES
# ================

calorie_array = []
calorie_array_sums = []
top_three_total_calorie_sums = 0

# ====
# MAIN
# ====

if __name__ == "__main__":
    calorie_array = get_calorie_inputs_func()
    calorie_array.sort(reverse=True)
    top_three_total_calorie_sums = calorie_array[0] + calorie_array[1] + calorie_array[2]
    print(top_three_total_calorie_sums)
