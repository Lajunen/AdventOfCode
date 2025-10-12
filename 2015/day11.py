def day11(p):
    input = "hxbxwxba"

    if p == 1:
        print("Day 11, Part 1 solution: " + find_next_password(input))
    
    if p == 2:
        print("Day 11, Part 2 solution: " + find_next_password(find_next_password(input)))

def find_next_password(previous):
    invalid_password = True
    new_password = previous
    while invalid_password:
        new_password = add_one_to_password(new_password)
        if is_password_valid(new_password):
            return new_password

def is_password_valid(pswd):
    if "i" in pswd or "o" in pswd or "l" in pswd:
        return False
    
    if not has_increment_of_three(pswd):
        return False
    
    if not has_two_pairs(pswd):
        return False
    
    return True

def has_two_pairs(pswd):
    i = 0
    pairs = 0

    while i < len(pswd) -1:
        if pswd[i] == pswd[i+1]:
            pairs += 1
            i += 1
        i += 1
    
    if pairs >= 2:
        return True
    else:
        return False

def has_increment_of_three(pswd):
    i = 0
    while i < len(pswd) - 2:
        if get_char_or_index(pswd[i]) + 1 == get_char_or_index(pswd[i+1]) and get_char_or_index(pswd[i+1]) + 1 == get_char_or_index(pswd[i+2]):
            return True
        i += 1
    return False

def add_one_to_password(pswd):
    new_pswd = ""

    i = 7
    carry_one = True

    while i >= 0:
        if carry_one:
            new_char = get_char_or_index(str(get_char_or_index(pswd[i]) + 1))
        else:
            new_char = get_char_or_index(str(get_char_or_index(pswd[i])))
        
        if new_char != "a" and carry_one:
            carry_one = False

        new_pswd = new_char + new_pswd
        
        i -= 1
    
    return new_pswd

def get_char_or_index(ch):
    available_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    i = 0
    while i < len(available_chars):
        if ch.isnumeric():
            if int(ch) > 25:
                return "a"
            else:
                return available_chars[int(ch)]
        else:
            if available_chars[i] == ch:
                return i
        i += 1
    return 0
