from copy import deepcopy
import readfile

def day25(p):
    data = readfile.read_line(25)

    target = get_target_from_input(data)

    if p == 1:
        print("Day 25, Part 1 solution: " + str(part_one([1,1], target, 20151125)))

def part_one(loc, tar, val):
    result_found = False
    result = [[], -1]
    while not result_found:
        if result[1] == -1:
            result = calculate_codes(loc, tar, val, 1)
        else:
            start_location = deepcopy(result[0])
            result = calculate_codes(start_location, tar, result[1], 1)
        if result[0][0] == tar[0] and result[0][1] == tar[1]:
            result_found = True
    return result[1]
    
def calculate_codes(location, target, value, step):
    if location[0] == 1 and location[1] == 1:
        location_value = value
    else:
        location_value = (value*252533)%33554393

    if step == 900:
        return [location, value]

    if location[0] == target[0] and location[1] == target[1]:
        return [location, location_value]
    else:
        if location[0] == 1:
            return calculate_codes([location[1] + 1, 1], target, location_value, step + 1)
        else:
            return calculate_codes([location[0] - 1, location[1] + 1], target, location_value, step + 1)

def get_target_from_input(data):
    target = [0, 0]
    data = data.replace(",", "")
    data = data.replace(".", "")
    parts = data.split(" ")

    for i in range(0, len(parts), 1):
        if parts[i] == "row":
            target[0] = int(parts[i+1])
        if parts[i] == "column":
            target[1] = int(parts[i+1])
    
    return target
