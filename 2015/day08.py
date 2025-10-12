import readfile

def day08(p):
    data = readfile.read_lines(8)
    ## data = ["\"\\x27\"", "\"\\x99a\""]

    if p == 1:
        print("Day 8, Part 1 solution: " + str(part_one(data)))
    
    if p == 2:
        print("Day 8, Part 2 solution: " + str(part_two(data)))

def part_one(data):
    code_chars = 0
    mem_chars = 0

    for dataline in data:
        code_chars += len(dataline)
        mem_chars += get_mem_chars(dataline)
    
    print("total code chars: " + str(code_chars) + " and mem chars: " + str(mem_chars))
    return code_chars - mem_chars

def part_two(data):
    code_chars = 0
    encoded = 0

    for dataline in data:
        code_chars += len(dataline)
        encoded += get_encoded_chars(dataline)
    
    return encoded - code_chars

def get_encoded_chars(s):
    return 2 + len(s) + s.count("\\") + s.count("\"")

def get_mem_chars(s):
    ## first we strip " from beginning and the end
    new_str = s[1:len(s)-1]

    extra_chars = 0

    i = 0
    while i < len(new_str):
        if new_str[i] == "\\":
            if i < len(new_str) - 1:
                if new_str[i+1] == "\\" or new_str[i+1] == "\"":
                    extra_chars += 1
                    i += 1
                else:
                    if i < len(new_str) - 3:
                        if new_str[i+1] == "x" and is_hexa(new_str[i+2]) and is_hexa(new_str[i+3]):
                            extra_chars += 3
                            i += 3
        i += 1

    return len(new_str) - extra_chars

def is_hexa(ch):
    if ch.isnumeric() or ch == "a" or ch == "b" or ch == "c" or ch == "d" or ch == "e" or ch == "f":
        return True
    else:
        return False