import readfile

def day03(p):
    triangles_raw_data = readfile.read_lines(3)

    triangle_data = parse_data(triangles_raw_data)

    if p == 1:
        print("Day 3, Part 1 solution: " + str(part_one(triangle_data)))
    if p == 2:
        print("Day 3, Part 2 solution: " + str(part_two(triangle_data)))


def part_one(triangles):
    possible = 0

    for tri in triangles:
        if is_possible(tri):
            possible += 1
    
    return possible

def part_two(triangles):
    possible = 0
    tr1 = []
    tr2 = []
    tr3 = []
    side = 1

    for row in triangles:
        tr1.append(row[0])
        tr2.append(row[1])
        tr3.append(row[2])
        if side < 3:
            side += 1
        else:
            tr1.sort()
            tr2.sort()
            tr3.sort()
            if is_possible(tr1):
                possible += 1
            if is_possible(tr2):
                possible += 1
            if is_possible(tr3):
                possible += 1
            side = 1
            tr1 = []
            tr2 = []
            tr3 = []
    
    return possible

def parse_data(data):
    parsed_data = []
    for line in data:
        new_line = []
        line_parts = line.split(" ")
        for part in line_parts:
            if part != "":
                new_line.append(int(part))
        parsed_data.append(new_line)
    
    return parsed_data

def is_possible(triangle):
    triangle.sort()
    if triangle[0] + triangle[1] > triangle[2]:
        return True
    return False
