import readfile

def day02(part):
    con = readfile.read_lines(2)

    if part == 1:
        print("Day 2, Part 1 solution: " + str(part_one(con)))
    
    if part == 2:
        print("Day 2, Part 2 solution: " + str(part_two(con)))
    
def part_one(lines):
    paper = 0
    for line in lines:
        params = line.split("x")
        side_one = int(params[0])*int(params[1])
        side_two = int(params[1])*int(params[2])
        side_three = int(params[2])*int(params[0])
        smallest = side_one
        if side_two < smallest:
            smallest = side_two
        if side_three < smallest:
            smallest = side_three
        paper += 2*side_one + 2*side_two + 2*side_three + smallest
    
    return paper

def part_two(lines):
    ribbon = 0
    for line in lines:
        params = line.split("x")
        smallest = 2*int(params[0]) + 2*int(params[1])
        if 2*int(params[1]) + 2*int(params[2]) < smallest:
            smallest = 2*int(params[1]) + 2*int(params[2])
        if 2*int(params[2]) + 2*int(params[0]) < smallest:
            smallest = 2*int(params[2]) + 2*int(params[0])
        ribbon += smallest + int(params[0])*int(params[1])*int(params[2])
    
    return ribbon