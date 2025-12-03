import hashlib
from copy import deepcopy

longest = -1

def day17(p):
    global longest

    inp = "bwnlcvfs"

    start_location = [0, 0]

    if p == 1:
        print("Day 17, Part 1 solution: " + find_shortest_route(start_location, inp, ""))
    if p == 2:
        find_longest_route(0, 0, inp, "")
        print("Day 17, Part 2 solution: " + str(longest))

def find_shortest_route(loc, inp, path):
    next_steps = []
    next_steps.append([loc, inp, path])

    while True:
        next_level = []

        for step in next_steps:
            room_hash = hashlib.md5((step[1] + step[2]).encode()).hexdigest().lower()
            if step[0][1] > 0 and room_hash[0] in "bcdef":
                next_level.append([[step[0][0], step[0][1] - 1], inp, step[2] + "U"])
            if step[0][1] < 3 and room_hash[1] in "bcdef":
                if step[0][0] == 3 and step[0][1] + 1 == 3:
                    return step[2] + "D"
                next_level.append([[step[0][0], step[0][1] + 1], inp, step[2] + "D"])
            if step[0][0] > 0 and room_hash[2] in "bcdef":
                next_level.append([[step[0][0] - 1, step[0][1]], inp, step[2] + "L"])
            if step[0][0] < 3 and room_hash[3] in "bcdef":
                if step[0][0] + 1 == 3 and step[0][1] == 3:
                    return step[2] + "R"
                next_level.append([[step[0][0] + 1, step[0][1]], inp, step[2] + "R"])
        
        next_steps = deepcopy(next_level)

def find_longest_route(x_loc, y_loc, inp, path):
    global longest

    if x_loc == 3 and y_loc == 3:
        if longest == -1 or len(path) > longest:
            longest = len(path)
        return

    room_hash = hashlib.md5((inp + path).encode()).hexdigest().lower()
    if y_loc > 0 and room_hash[0] in "bcdef":
        find_longest_route(x_loc, y_loc - 1, inp, path + "U")
    if y_loc < 3 and room_hash[1] in "bcdef":
        find_longest_route(x_loc, y_loc + 1, inp, path + "D")
    if x_loc > 0 and room_hash[2] in "bcdef":
        find_longest_route(x_loc - 1, y_loc, inp, path + "L")
    if x_loc < 3 and room_hash[3] in "bcdef":
        find_longest_route(x_loc + 1, y_loc, inp, path + "R")
    
    return
