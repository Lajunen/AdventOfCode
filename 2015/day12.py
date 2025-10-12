import readfile

def day12(p):
    data = readfile.read_json(12)

    if p == 1:
        print("Day 12, Part 1 solution: " + str(count_all(data, p)))
    
    if p == 2:
        print("Day 12, Part 2 solution: " + str(count_all(data, p)))

def count_all(data, p):
    value = 0
    for entry in data:
        if type(entry) == list:
            value += count_array(entry, p)
        if type(entry) == dict:
            value += count_dict(entry, p)
        if type(entry) == int:
            value += int(entry)
    
    return value

def count_array(arr, p):
    value = 0
    for entry in arr:
        if type(entry) == list:
            value += count_array(entry, p)
        if type(entry) == dict:
            value += count_dict(entry, p)
        if type(entry) == int:
            value += entry
    
    return value

def count_dict(dic, p):
    value = 0
    if p == 2:
        for val in dic.values():
            if val == "red":
                return 0

    for val in dic.values():
        if type(val) == list:
            value += count_array(val, p)
        if type(val) == dict:
            value += count_dict(val, p)
        if type(val) == int:
            value += val
    
    return value
