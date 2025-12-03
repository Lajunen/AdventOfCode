import readfile

def day02(p):
    data_ranges = get_ranges(readfile.read_line(2))
    test_ranges = [[11, 22], [95, 115], [998, 1012], [1188511880, 1188511890], [222220, 222224], [446443, 446449], [38593856, 38593862], [1698522, 1698528]]
    test_ranges_2 = [[998,1012]]
    
    if p == 1:
        print("Day 02, part 1 solution: " + str(part_one(data_ranges)))
    if p == 2:
        print("Day 02, part 2 solution: " + str(part_two(data_ranges)))

def part_one(ranges):
    result = 0
    for r in ranges:
        for id in range(r[0], r[1] + 1, 1):
            if len(str(id))%2 == 0:
                s = str(id)
                if str(id)[0:int(len(str(id)) / 2)] == str(id)[int(len(str(id)) / 2):]:
                    result += id

    return result

def part_two(ranges):
    result = 0
    for r in ranges:
        for id in range(r[0], r[1] + 1, 1):
            if invalid_id(id):
                ## print(str(id) + " was found invalid!")
                result += id
    
    return result

def invalid_id(id_to_check):
    for seq_length in range(1, int(len(str(id_to_check)) / 2) + 1, 1):
        seq_to_find = str(id_to_check)[0:seq_length]
        ## print("id: " + str(id_to_check) + " // seqment to find: " + seq_to_find + " // length: " + str(seq_length))
        seq_repeats = True
        for index_to_check in range(seq_length, len(str(id_to_check)), seq_length):
            if str(id_to_check)[index_to_check:index_to_check + seq_length] != seq_to_find:
                seq_repeats = False
        if seq_repeats:
            return True
    
    return False


def get_ranges(data):
    result = []

    ranges = data.split(",")
    for r in ranges:
        parts = r.split("-")
        new_range = [int(parts[0]), int(parts[1])]
        result.append(new_range)

    return result

day02(2)