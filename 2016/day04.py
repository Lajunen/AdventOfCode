import readfile
from collections import Counter

def day04(p):
    data = readfile.read_lines(4)
    test = ["aaaaa-bbb-z-y-x-123[abxyz]", "a-b-c-d-e-f-g-h-987[abcde]", "not-a-real-room-404[oarel]", "totally-real-room-200[decoy]"]

    if p == 1:
        print("Day 4, Part 1 solution: " + str(part_one(data)))
    if p == 2:
        print("Day 4, Part 2 solution: " + str(part_two(data)))

def part_one(sec_ids):
    real = 0

    for line in sec_ids:
        real_room, id = verify_room(line)
        if real_room:
            real += id

    return real

def part_two(sec_ids):
    storage_room_id = 0
    for line in sec_ids:
        name, id, _ = get_room_info(line)
        name = name[:len(name)-1]
        true_name = decrypt_name(name, id)
        if "north" in true_name:
            storage_room_id = id
    
    return storage_room_id

def decrypt_name(name, id):
    decrypted = ""
    for ch in name:
        if ch == "-":
            decrypted += " "
        else:
            decrypted += rotate(ch, id)
    return decrypted

def rotate(ch, id):
    alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    current_id_number = 0
    for alp in range(0, len(alphabets), 1):
        if alphabets[alp] == ch:
            current_id_number = alp
    return alphabets[(current_id_number + id)%26]


    

def verify_room(info):
    name, id, checksum = get_room_info(info)
    name = name.replace("-", "")
    created_checksum = create_checksum(name)
    return created_checksum == checksum, id

def create_checksum(name):
    c = Counter(name)
    counts = c.items()
    vals = sorted(counts, key=lambda x: (-x[1], x[0]))
    check_gen = ""
    for i in range(0, 5, 1):
        check_gen += vals[i][0]

    return check_gen

def get_room_info(info):
    parts = info.split("[")
    name = parts[0][:len(parts[0]) - 3]
    id = int(parts[0][len(parts[0]) - 3:])
    checksum = parts[1][:len(parts[1]) - 1]
    
    return name, id, checksum