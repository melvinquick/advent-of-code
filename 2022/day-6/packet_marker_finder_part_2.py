# =========
# LIBRARIES
# =========

import os
import sys

# =========
# FUNCTIONS
# =========

# Function to get the datastream info of the elves' signal
def get_datastream_func():
    # Local Variables
    datastream = []

    # Local Main Code
    datastream_file = open(os.path.join(sys.path[0], "input.txt"), "r")
    for data in datastream_file:
        datastream.append(data.replace("\n", ""))
    datastream_file.close()
    return datastream

# Function to split the datastream into individual characters
def split_datastream_func(datastream):
    # Local Variables
    new_datastream = []

    # Local Main Code
    for data in datastream:
        for char in data:
            new_datastream.append(char)
    return new_datastream

# Function to find the number of characters it takes to get to the end of the first four character buffer
def find_buffer_characters_func(datastream):
    # Local Variables
    chars = []
    counter = 0

    # Local Main Code
    while counter <= len(datastream)-4:
        chars = [datastream[counter], datastream[counter+1], datastream[counter+2], datastream[counter+3]]
        if chars[0] == chars[1] or chars[0] == chars[2] or chars[0] == chars[3] or chars[1] == chars[2] or chars[1] == chars[3] or chars[2] == chars[3]:
            counter += 1
        else:
            return counter+4
    return -1

# Function to find the number of characters it takes to get end of the start of message marker
def find_message_buffer_characters_func(datastream):
    # Local Variables
    chars = []
    counter_1 = 0
    counter_2 = 0
    char_counter = 0

    # Local Main Code
    while counter_2 <= len(datastream)-14:
        counter_1 = counter_2
        chars = []
        char_counter = 0
        while counter_1 <= counter_2+13:
            chars.append(datastream[counter_1])
            counter_1 += 1
        for char in chars:
            char_counter += chars.count(char)
        if char_counter > 14:
            counter_2 += 1
        else:
            return counter_2+14
    return -1


# ================
# GLOBAL VARIABLES
# ================

datastream = []
chars_to_message_buffer = 0


# ====
# MAIN
# ====

if __name__ == "__main__":
    datastream = get_datastream_func()
    datastream = split_datastream_func(datastream)
    chars_to_message_buffer = find_message_buffer_characters_func(datastream)
    print(chars_to_message_buffer)
