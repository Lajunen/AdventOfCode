import readfile

def day03(p):
    banks = readfile.read_lines(3)

    if p == 1:
        print("Day 03, part 1 solution: " + str(part_one(banks)))
    if p == 2:
        print("Day 03, part 2 solution: " + str(part_two(banks)))
    
def part_one(banks):
    sum = 0
    for bank in banks:
        sum += int(find_max_joltage(bank, 2))
    
    return sum

def part_two(banks):
    sum = 0
    for bank in banks:
        sum += int(find_max_joltage(bank, 12))
    
    return sum

def find_max_joltage(bank, amount):
    for dig in range(9, 0, -1):
        for ind in range(0, len(bank) - amount + 1, 1):
            if str(dig) == bank[ind]:
                if amount > 1:
                    return bank[ind] + find_max_joltage(bank[ind + 1:], amount - 1)
                else:
                    return bank[ind]

day03(2)