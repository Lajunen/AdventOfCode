import readfile

def day18(p):
    grid = modify(readfile.read_lines(18))

    if p == 1:
        print("Day 18, Part 1 solution: " + str(part_one(grid, 100)))
    
    if p == 2:
        print("Day 18, Part 2 solution: " + str(part_two(grid, 100)))


def part_one(grid, steps):
    for i in range(0, steps):
        grid = take_step(grid, 1)

    return calculate_on_lights(grid)

def part_two(grid, steps):
    grid[0][0] = 1
    grid[0][-1] = 1
    grid[-1][0] = 1
    grid[-1][-1] = 1

    for i in range(0, steps):
        grid = take_step(grid, 2)
    
    return calculate_on_lights(grid)

def take_step(grid, part):
    new_grid = []

    for y in range(0, len(grid)):
        new_line = []
        for x in range(0, len(grid[0])):
            neighbours_on = 0

            ## getting check area (around the spot)
            min_y, max_y, min_x, max_x = 0, 0, 0, 0
            if y == 0:
                ## top row
                min_y = 0
            else:
                min_y = y-1
            if x == 0:
                ## left column
                min_x = 0
            else:
                min_x = x-1
            if y == len(grid) - 1:
                ## bottom row
                max_y = y
            else:
                max_y = y + 1
            if x == len(grid[0]) - 1:
                ## right column
                max_x = x
            else:
                max_x = x + 1

            ## checking the area (excluding the spot we are on)                
            for check_y in range(min_y, max_y + 1):
                for check_x in range(min_x, max_x + 1):
                    if grid[check_y][check_x] == 1 and (check_x != x or check_y != y):
                        neighbours_on += 1
            
            if grid[y][x] == 0:
                if neighbours_on == 3:
                    new_line.append(1)
                else:
                    new_line.append(0)
            if grid[y][x] == 1:
                if neighbours_on == 2 or neighbours_on == 3:
                    new_line.append(1)
                else:
                    new_line.append(0)

        new_grid.append(new_line)
    
    if part == 2:
        new_grid[0][0] = 1
        new_grid[0][-1] = 1
        new_grid[-1][0] = 1
        new_grid[-1][-1] = 1

    return new_grid

def calculate_on_lights(grid):
    lights_on = 0

    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid[y][x] == 1:
                lights_on += 1
    
    return lights_on

def modify(grid):
    new_grid = []
    for line in grid:
        new_line = []
        for ch in line:
            if ch == ".":
                new_line.append(0)
            if ch == "#":
                new_line.append(1)
        new_grid.append(new_line)
    
    return new_grid
