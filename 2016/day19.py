from copy import deepcopy

def day19(p):
    elves = 3014603
    test_elves = 5

    elf_list = make_elf_list(elves)

    if p == 1:
        print("Day 19, Part 1 solution: " + str(part_one_play_game(elf_list)))
    if p == 2:
        print("Day 19, Part 2 solution: " + str(part_two_play_game(elf_list)))

def part_two_play_game(elves):
    turn = 0
    while len(elves) > 1:
        elves_left = []
        print(str(len(elves)))

        if len(elves) == 5:
            return elves[1]
        if len(elves) == 4:
            return elves[0]
        if len(elves) == 3:
            return elves[2]
        if len(elves) == 2:
            return elves[0]
        if len(elves)%2 == 0:
            for i in range(int(len(elves)/3) + 1, int(len(elves)/2) + 1, 1):
                elves_left.append(deepcopy(elves[i]))
            for i in range(int(len(elves)/2) + 2, len(elves), 3):
                elves_left.append(deepcopy(elves[i]))
            for i in range(0, int(len(elves)/3) + 1, 1):
                elves_left.append(deepcopy(elves[i]))
        else:
            for i in range(int(len(elves)/3) + 1, int(len(elves)/2) + 1, 1):
                elves_left.append(deepcopy(elves[i]))
            for i in range(int(len(elves)/2) + 1, len(elves), 3):
                elves_left.append(deepcopy(elves[i]))
            for i in range(0, int(len(elves)/3) + 1, 1):
                elves_left.append(deepcopy(elves[i]))

        elves = deepcopy(elves_left)
    

def play_round(elves):
    elves_left = deepcopy(elves)

    if len(elves) == 2:
        return elves_left[0]
    
    if len(elves)%2 == 1:
        elves_left.pop(int(len(elves)/2))
        
        elves_left.append(deepcopy(elves[0]))
        elves_left.pop(0)

        return elves_left
    else:
        elves_left.pop(int(len(elves)/2) + 1)

        elves_left.append(deepcopy(elves[0]))
        elves_left.pop(0)

        return elves_left

def part_one_play_game(elves):
    while len(elves) > 1:
        elves_left = []
        if len(elves)%2 == 1:
            elves_left.append(deepcopy(elves[-1]))
            for i in range(0, len(elves)-1, 2):
                elves_left.append(deepcopy(elves[i]))
        else:
            for i in range(0, len(elves), 2):
                elves_left.append(deepcopy(elves[i]))
        elves = deepcopy(elves_left)
    
    return elves[0]

def make_elf_list(amount):
    elves = []

    for i in range(1, amount + 1, 1):
        elves.append(i)
    
    return elves

day19(2)