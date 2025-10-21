import readfile

def day08(p):
    input = readfile.read_lines(8)
    ##test_input = ["rect 1x1", "rotate row y=0 by 53"]

    screen = get_screen()

    if p == 1:
        print("Day 8, Part 1 solution: " + str(part_one(screen, input)))
    if p == 2:
        print("Day 8, Part 2 solution:")
        part_two(screen, input)

def part_one(screen, input):
    for line in input:
        execute_command(line, screen)
    
    lights = 0
    for row in range(0, len(screen), 1):
        for col in range(0, len(screen[row]), 1):
            if screen[row][col] == "X":
                lights += 1
    
    return lights

def part_two(screen, input):
    for line in input:
        execute_command(line, screen)
    
    show_screen(screen)

def execute_command(command, screen):
    info = command.split(" ")
    if info[0] == "rect":
        coords = info[1].split("x")
        rect(int(coords[0]), int(coords[1]), screen)
    elif info [0] == "rotate":
        if info[1] == "row":
            y_parts = info[2].split("=")
            rotate_row(int(y_parts[1]), int(info[4]), screen)
        elif info[1] == "column":
            x_parts = info[2].split("=")
            rotate_column(int(x_parts[1]), int(info[4]), screen)

def rect(x, y, screen):
    for row in range(0, y, 1):
        for col in range(0, x, 1):
            screen[row][col] = "X"

def rotate_row(y, amount, screen):
    for rotation in range(0, amount):
        screen[y].insert(0, screen[y][-1])
        screen[y].pop(50)

def rotate_column(x, amount, screen):
    new_col = []
    for y in range(0, 6):
        new_col.append(screen[y][x])
    for roration in range(0, amount):
        new_col.insert(0, new_col[-1])
        new_col.pop(6)
    for y in range(0, 6):
        screen[y][x] = new_col[y]

def show_screen(screen):
    print("+" + "-"*50 + "+")
    for row in screen:
        print("|" + "".join(row) + "|")
    print("+" + "-"*50 + "+")

def get_screen():
    screen = []
    for row in range(0, 6, 1):
        new_row = []
        for col in range(0, 50, 1):
            new_row.append(" ")
        screen.append(new_row)
    
    return screen
