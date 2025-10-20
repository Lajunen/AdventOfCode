import readfile
from copy import deepcopy
from collections import Counter

def day06(p):
    data = readfile.read_lines(6)

    if p == 1:
        print("Day 6, Part 1 solution: " + str(part_one(data)))
    if p == 2:
        print("Day 6, Part 2 solution: " + str(part_two(data)))

def part_one(data):
    organized_data = []
    for col in range(0, 8, 1):
        new_col = []
        for row in data:
            new_col.append(row[col])
        organized_data.append(deepcopy(new_col))
    
    message = []
    for index in range(0, len(organized_data), 1):
        col_char = Counter(organized_data[index])
        char = col_char.most_common(1)
        message.append(deepcopy(char[0][0]))
    
    message = "".join(message)

    return message

def part_two(data):
    organized_data = []
    for col in range(0, 8, 1):
        new_col = []
        for row in data:
            new_col.append(row[col])
        organized_data.append(deepcopy(new_col))
    
    message = []
    for index in range(0, len(organized_data), 1):
        col_char = Counter(organized_data[index])
        char = col_char.most_common()
        message.append(deepcopy(char[-1][0]))
    
    message = "".join(message)

    return message
