def day16(p):
    inp = "10111100110001111"

    if p == 1:
        print("Day 16, Part 1 solution: " + fill_disc(inp, 272))
    if p == 2:
        print("Day 16, Part 2 solution: " + fill_disc(inp, 35651584))

def fill_disc(inp, size):
    res = inp

    while len(res) <= size:
        part_a = res

        ## constructing part b
        part_b = ""
        for i in range(len(res) - 1, -1 , -1):
            if res[i] == "0":
                part_b += "1"
            else:
                part_b += "0"
        
        res = part_a + "0" + part_b

    return calculate_checksum(res[:size])

def calculate_checksum(data):
    checksum = data

    while len(checksum)%2 == 0:
        new_checksum = ""
        for i in range(1, len(checksum), 2):
            if checksum[i] == checksum[i-1]:
                new_checksum += "1"
            else:
                new_checksum += "0"
        checksum = new_checksum
    
    return checksum
