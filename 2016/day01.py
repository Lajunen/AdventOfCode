import readfile
from copy import deepcopy

def day01(p):
    route_raw = readfile.read_line(1)
    route = parse_data(route_raw)

    if p == 1:
        print("Day 1, Part 1 solution: " + str(walk_route(route, 1)))
    if p == 2:
        print("Day 1, Part 2 solution: " + str(walk_route(route, 2)))

def walk_route(route, part):
    ## variables for both parts
    heading = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    facing = 0
    location = [0,0]

    ## part two added variables
    locations_visited = []
    locations_visited.append(deepcopy(location))
    part2_finished = False

    for step in route:
        if step[0] == "R":
            facing += 1
            if facing == 4:
                facing = 0
        elif step[0] == "L":
            facing -= 1
            if facing == -1:
                facing = 3
        for i in range(0, step[1], 1):
            location[0] = location[0] + (1*heading[facing][0])
            location[1] = location[1] + (1*heading[facing][1])
            if part == 2:
                if location in locations_visited:
                    part2_finished = True
                    break
                else:
                    locations_visited.append(deepcopy(location))
        if part2_finished:
            break


    distance = 0
    if location[0] < 0:
        distance += location[0] * (-1)
    else:
        distance += location[0]
    if location[1] < 0:
        distance += location[1] * (-1)
    else:
        distance += location[1]

    return distance  

def parse_data(data):
    data = data.replace(",", "")
    
    route = []
    parts = data.split(" ")
    for part in parts:
        step = []
        step.append(part[0:1])
        step.append(int(part[1:]))
        route.append(step)
    
    return route
