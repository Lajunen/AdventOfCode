import readfile

## For this days tasks I used a simple loop to iterate through the
## input string character at a time and updating floor.
## On day 2 I checked the floor after each update to return at the
## first time enter basement (floor being lower than 0)

def day01(part):
    con = readfile.read_line(1)

    if part == 1:
        print("Day 1, Part 1 solution: " + str(part_one(con)))
    if part == 2:
        print("Day 1, Part 2 solution: " + str(part_two(con)))
    
def part_one(st):
    floor = 0
    for char in st:
        if char == "(":
            floor += 1
        if char == ")":
            floor -= 1
    return floor

def part_two(st):
    floor = 0
    step = 1
    for char in st:
        if char == "(":
            floor += 1
        if char == ")":
            floor -= 1
        if floor < 0:
            return step
        step += 1
