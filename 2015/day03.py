import readfile

def day03(p):
    con = readfile.read_line(3)

    if p == 1:
        print("Day 3, Part 1 solution: " + str(part_one(con)))
    
    if p == 2:
        print("Day 3, Part 2 solution: " + str(part_two(con)))

def part_one(con):
    x = 0
    y = 0
    locs = [[x, y]]
    presents = 1
    for char in con:
        if char == "^":
            y -= 1
        if char == "v":
            y += 1
        if char == "<":
            x -= 1
        if char == ">":
            x += 1
        cur_loc = [x, y]
        if cur_loc not in locs:
            presents += 1
            locs.append(cur_loc)
    
    return presents

def part_two(con):
    xs = 0
    ys = 0
    xr = 0
    yr = 0
    turn = "s"
    locs = [[xs, ys]]
    presents = 1
    for char in con:
        if turn == "s":
            if char == "^":
                ys -= 1
            if char == "v":
                ys += 1
            if char == "<":
                xs -= 1
            if char == ">":
                xs += 1
            cur_loc = [xs, ys]
            if cur_loc not in locs:
                presents += 1
                locs.append(cur_loc)
            turn = "r"
        else:
            if char == "^":
                yr -= 1
            if char == "v":
                yr += 1
            if char == "<":
                xr -= 1
            if char == ">":
                xr += 1
            cur_loc = [xr, yr]
            if cur_loc not in locs:
                presents += 1
                locs.append(cur_loc)
            turn = "s"
    
    return presents


