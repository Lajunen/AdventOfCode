import json

def read_line(d):
    filename = "day"
    if d >= 10:
        filename += str(d)
    else:
        filename += "0" + str(d)
    filename += "-input.txt"
    
    file = open(filename, "r")
    content = file.read()

    file.close()

    return content

def read_lines(d):
    filename = "day"
    content = []

    if d >= 10:
        filename += str(d)
    else:
        filename += "0" + str(d)
    filename += "-input.txt"

    with open(filename, "r") as file:
        lines = file.readlines()
    
    for line in lines:
        content.append(line.replace("\n", ""))
    
    return content

def read_json(d):
    filename = "day"

    if d >= 10:
        filename += str(d)
    else:
        filename += "0" + str(d)
    filename += "-input.txt"

    with open(filename, "r") as file:
        data = json.load(file)
    
    return data