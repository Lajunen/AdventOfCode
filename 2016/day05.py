import hashlib
import os

def day05(p):
    input = "wtnhxymk"

    if p == 1:
        print("Day 5, Part 1 solution: " + part_one(input))
    if p == 2:
        print("Day 5, Part 2 solution: " + part_two(input))
    
def part_one(input):
    password = ""
    cont = -1
    for i in range(0, 8, 1):
        while len(password) < 8:
            if cont == -1:
                correct, cont, digit = crack_next(input, 0, 1)
            if correct:
                password += str(digit)
                show_password(password)
                correct = False
            else:
                correct, cont, digit = crack_next(input, int(cont) + 1, 1)
    
    return password

def part_two(input):
    password = ["_"]*8
    cont = -1
    password_complete = False

    while not password_complete:
        if cont == -1:
            correct, cont, digit = crack_next(input, 0, 2)
        if correct:
            valid, digit_num, digit_pos = part_two_break_digit(digit)
            if valid:
                print(digit_pos)
                pos = int(digit_pos)
                if password[pos] == "_":
                    password[pos] = digit_num
                still_incomplete = False
                for pos in password:
                    if pos == "_":
                        still_incomplete = True
                show_password("".join(password))
            correct = False
            if not still_incomplete:
                password_complete = True
        else:
            correct, cont, digit = crack_next(input, int(cont) + 1, 2)
    
    return "".join(password)

def crack_next(input, step, part):
    to_hash = input + str(step)
    result = hashlib.md5(to_hash.encode())
    if result.hexdigest().startswith("00000"):
        if part == 1:
            return True, str(step), result.hexdigest()[5]
        if part == 2:
            return True, str(step), result.hexdigest()[5:7]
    else:
        if step%900 == 0:
            return False, str(step), ""
        else:
            return crack_next(input, step + 1, part)

def part_two_break_digit(digit):
    pos = digit[:1]
    num = digit[1:]
    if pos.isdigit():
        pos_num = int(pos)
        if pos_num >= 0 and pos_num <= 7:
            return True, num, pos
    return False, num, pos

def show_password(pswd):
    os.system('clear')
    print("Password: " + pswd)
