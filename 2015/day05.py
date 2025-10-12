import readfile

def day05(p):
    con = readfile.read_lines(5)

    if p == 1:
        print("Day 5, Part 1 solution: " + str(part_one(con)))
    
    if p == 2:
        print("Day 5, Part 2 solution: " + str(part_two(con)))

def part_one(con):
    nicelist = []

    for line in con:
        if line.lower().count("a") + line.lower().count("e") + line.lower().count("i") + line.lower().count("o") + line.lower().count("u") >= 3:
            check_two = False
            ind = 0
            last_char = ""
            for char in line:
                if char == last_char:
                    check_two = True
                last_char = char
            if check_two:
                if "ab" not in line and "cd" not in line and "pq" not in line and "xy" not in line:
                    nicelist.append(line)
    
    return len(nicelist)

def part_two(con):
    nicelist = []

    for line in con:
        check_one = False
        for i in range(len(line)-3):
            if line[i:i+2] in line[i+2:]:
                check_one = True

        check_two = False
        for i in range(len(line)-2):
            if line[i] == line[i+2]:
                check_two = True

        if check_one and check_two:
            nicelist.append(line)
    
    return len(nicelist)
        
