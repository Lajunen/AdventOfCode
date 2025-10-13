import readfile

def day16(p):
    data = readfile.read_lines(16)

    persons = parse_data(data)

    if p == 1:
        print("Day 16, Part 1 solution: " + str(find_sue(persons, p)))
    
    if p == 2:
        print("Day 16, Part 2 solution: " + str(find_sue(persons, p)))
    

def find_sue(persons, p):
    ## running through filters
    sues_left = filter_exact(persons)
    sues_left = filter_part_conditioned(sues_left, p)

    
    return sues_left[0].id_number

def filter_part_conditioned(persons, p):
    ## things that need to be found, or no info about
    ## part 1: cats 7, pomeranians 3, goldfish 5, trees 3
    ## part 2: cats > 7, trees > 3, pomeranians < 2, goldfish < 5
    new_sues = []

    for sue in persons:
        contradiction_found = False
        for info_bit in sue.info:
            if p == 1 and ((info_bit[0] == "cats" and info_bit[1] != 7) or (info_bit[0] == "pomeranians" and info_bit[1] != 3) or (info_bit[0] == "goldfish" and info_bit[1] != 5) or (info_bit[0] == "trees" and info_bit[1] != 3)):
                contradiction_found = True
            if p == 2 and ((info_bit[0] == "cats" and info_bit[1] <= 7) or (info_bit[0] == "pomeranians" and info_bit[1] >= 3) or (info_bit[0] == "goldfish" and info_bit[1] >= 5) or (info_bit[0] == "trees" and info_bit[1] <= 3)):
                contradiction_found = True
        if not contradiction_found:
            new_sues.append(sue)
    
    return new_sues

def filter_exact(persons):
    ## things that need to be found, or no info about
    ## children 3, samoyeds 2, akitas 0, vizslas 0, cars 2, perfumes 1
    new_sues = []

    for sue in persons:
        contradiction_found = False
        for info_bit in sue.info:
            if (info_bit[0] == "children" and info_bit[1] != 3) or ((info_bit[0] == "samoyeds" or info_bit[0] == "cars") and info_bit[1] != 2) or ((info_bit[0] == "akitas" or info_bit[0] == "vizslas") and info_bit[1] != 0) or (info_bit[0] == "perfumes" and info_bit[1] != 1):
                contradiction_found = True
        if not contradiction_found:
            new_sues.append(sue)
    
    return new_sues

def parse_data(data):
    persons = []
    for line in data:
        line = line.replace(":", "")
        line = line.replace(",", "")
        info_bits = line.split(" ")
        new_sue = person()
        new_sue.id_number = int(info_bits[1])
        new_info = []
        for a in range(2, len(info_bits), 2):
            new_info.append([info_bits[a], int(info_bits[a+1])])
        new_sue.info = new_info
        persons.append(new_sue)
    return persons

class person:
    id_number = 0
    info = []