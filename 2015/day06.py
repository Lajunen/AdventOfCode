import readfile

def day06(p):
    con = readfile.read_lines(6)

    lights = [[0]*1000]*1000

    if p == 1:
        print("Day 6, Part 1 solution: " + str(part_one(con)))
    
    if p == 2:
        print("Day 6, Part 2 solution: " + str(part_two(con)))

def part_one(instructions):
    lights = [[0 for x in range(1000)] for y in range(1000)]

    for instruction in instructions:
        insts = instruction.split(" ")
        if insts[0] == "turn":
            if insts[1] == "on":
                oper = "on"
            else:
                oper = "off"
            start_loc = insts[2].split(",")
            end_loc = insts[4].split(",")
        if insts[0] == "toggle":
            oper = "flip"
            start_loc = insts[1].split(",")
            end_loc = insts[3].split(",")

        start_x = int(start_loc[0])
        start_y = int(start_loc[1])
        end_x = int(end_loc[0])
        end_y = int(end_loc[1])

        operations = 0
        for x in range(start_x, end_x +1):
            for y in range(start_y, end_y +1):
                operations += 1
                if oper == "flip":
                    if lights[y][x] == 0:
                        lights[y][x] = 1
                    else:
                        lights[y][x] = 0
                if oper == "off":
                    lights[y][x] = 0
                if oper == "on":
                    lights[y][x] = 1
    
    lights_on = 0

    for x in range(0, 1000):
        for y in range(0, 1000):
            lights_on += lights[y][x]
    
    return lights_on

def part_two(instructions):
    lights = [[0 for x in range(1000)] for y in range(1000)]

    for instruction in instructions:
        insts = instruction.split(" ")
        if insts[0] == "turn":
            if insts[1] == "on":
                oper = "on"
            else:
                oper = "off"
            start_loc = insts[2].split(",")
            end_loc = insts[4].split(",")
        if insts[0] == "toggle":
            oper = "flip"
            start_loc = insts[1].split(",")
            end_loc = insts[3].split(",")

        start_x = int(start_loc[0])
        start_y = int(start_loc[1])
        end_x = int(end_loc[0])
        end_y = int(end_loc[1])

        operations = 0
        for x in range(start_x, end_x +1):
            for y in range(start_y, end_y +1):
                operations += 1
                if oper == "flip":
                    lights[y][x] += 2
                if oper == "off" and lights[y][x] > 0:
                    lights[y][x] -= 1
                if oper == "on":
                    lights[y][x] += 1
    
    lights_on = 0

    for x in range(0, 1000):
        for y in range(0, 1000):
            lights_on += lights[y][x]
    
    return lights_on
