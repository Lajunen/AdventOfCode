import readfile
from copy import deepcopy

def day15(p):
    raw_data = readfile.read_lines(15)

    discs = parse_data(raw_data)

    if p == 1:
        print("Day 15, Part 1 solutions: " + part_one(discs))
    if p == 2:
        new_disc = disc(len(discs) + 1, 11, 0)
        discs.append(deepcopy(new_disc))
        print("Day 15, Part 2 solution: " + part_one(discs))

def part_one(discs):
    time = 0

    while True:
        bounce = False
        for dis in discs:
            if (time + dis.floor + dis.pos)%dis.positions != 0:
                bounce = True
        if not bounce:
            return str(time)
        
        time += 1


def parse_data(data):
    discs = []

    for line in data:
        line = line.replace("," , "")
        line = line.replace(".", "")
        line = line.replace("#", "")

        info_bits = line.split(" ")
        new_disc = disc(int(info_bits[1]), int(info_bits[3]), int(info_bits[11]))
        discs.append(deepcopy(new_disc))
    
    return discs

class disc:
    floor = 0
    positions = 0
    pos = 0

    def __init__(self, floor, positions, pos):
        self.floor = floor
        self.positions = positions
        self.pos = pos
