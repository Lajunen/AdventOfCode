import readfile

def day02(p):
    instructions = readfile.read_lines(2)

    if p == 1:
        print("Day 2, Part 1 solution: " + get_code(instructions, 1))
    if p == 2:
        print("Day 2, Part 2 solution: " + get_code(instructions, 2))
    

def get_code(instructions, part):
    code = ""

    for line in instructions:
        if code == "":
            if part == 1:
                code += str(get_next_numpad(line, 5))
            if part == 2:
                code += get_next_keypad(line, "5")
        else:
            if part == 1:
                code += str(get_next_numpad(line, int(code[-1])))
            if part == 2:
                code += str(get_next_keypad(line, code[-1]))
    
    return code

def get_next_keypad(instructions, current_key):
    keypad = [["", "", "1", "", ""], ["", "2", "3", "4", ""], ["5", "6", "7", "8", "9"], ["", "A", "B", "C", ""], ["", "", "D", "", ""]]

    x = 0
    y = 0
    for y_index in range(0, len(keypad)):
        for x_index in range(0, len(keypad[0])):
            if keypad[y_index][x_index] == current_key:
                x = x_index
                y = y_index
    
    for ch in instructions:
        if ch == "U":
            if y > 0:
                if keypad[y - 1][x] != "":
                    y -= 1
                    current_key = keypad[y][x]
        elif ch == "R":
            if x < len(keypad[0]) - 1:
                if keypad[y][x + 1] != "":
                    x += 1
                    current_key = keypad[y][x]
        elif ch == "D":
            if y < len(keypad) - 1:
                if keypad[y + 1][x] != "":
                    y += 1
                    current_key = keypad[y][x]
        elif ch == "L":
            if x > 0:
                if keypad[y][x - 1] != "":
                    x -= 1
                    current_key = keypad[y][x]
    
    return current_key

def get_next_numpad(instructions, current_number):
    for ch in instructions:
        if ch == "U":
            if current_number - 3 >= 1:
                current_number -= 3
        elif ch == "R":
            if current_number != 3 and current_number != 6 and current_number != 9:
                current_number += 1
        elif ch == "D":
            if current_number + 3 <= 9:
                current_number += 3
        elif ch == "L":
            if current_number != 1 and current_number != 4 and current_number != 7:
                current_number -= 1
    
    return current_number
