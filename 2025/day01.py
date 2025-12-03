import readfile

def day01(p):
    turns = readfile.read_lines(1)
    turns_test = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    if p == 1:
        print("Day 01, part 1 answer: " + str(part_one(turns)))
    if p == 2:
        print("Day 01, part 2 answer: " + str(part_two(turns)))

def part_one(turns):
    pos = 50
    code = 0
    for tur in turns:
        if tur[0] == "L":
            pos -= int(tur[1:])
        else:
            pos += int(tur[1:])
        
        while pos < 0 or pos > 99:
            if pos < 0:
                pos += 100
            elif pos > 99:
                pos = pos%100
        if pos == 0:
            code += 1
    
    return code

def part_two(turns):
    pos = 50
    code = 0
    for tur in turns:
        for _ in range(0, int(tur[1:]), 1):
            if tur[0] == "L":
                pos -= 1
            else:
                pos += 1
            
            if pos < 0:
                pos += 100
            if pos > 99:
                pos = pos%100
            if pos == 0:
                code += 1
            
    return code

day01(2)