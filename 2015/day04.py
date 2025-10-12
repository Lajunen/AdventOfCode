import hashlib

def day04(p):
    input = "yzbqklnj"

    if p == 1:
        print("Day 4, Part 1 solution: " + str(find_hash(input, "00000")))
    if p == 2:
        print("Day 4, Part 2 solution: " + str(find_hash(input, "000000")))

def find_hash(sec_key, start):
    num = 0

    while num < 100000000:
        s = sec_key + str(num)
        res = hashlib.md5(s.encode())
        hexres = res.hexdigest()
        if hexres.startswith(start):
            return num
        num += 1

    return 0
