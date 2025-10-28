def day13(p):
    if p == 1:
        print("Day 13, Part 1 solution: " + str(solve_maze((31, 39), 1350, p)))
    if p == 2:
        print("Day 13, Part 2 solution: " + str(solve_maze((99, 99), 1350, p)))

def solve_maze(goal, task_input, part):
    location = [0, [1, 1]]

    visited = []
    visited.append([1, 1])

    open_rooms = []

    queue = []
    queue.append(location)

    while len(queue) > 0:
        ## taking info from queue to more readable format
        cur_x = queue[0][1][0]
        cur_y = queue[0][1][1]
        cur_step = queue[0][0]

        if part == 2 and cur_step > 50:
            return len(open_rooms)

        if [cur_x, cur_y] not in open_rooms:
            open_rooms.append([cur_x, cur_y])

        ## checking if reached the goal
        if goal[0] == cur_x and goal[1] == cur_y:
            return cur_step

        ## moves to each open direction
        ## checking left room
        if cur_x > 0:
            if [cur_x - 1, cur_y] not in visited:
                visited.append([cur_x - 1, cur_y])
                if is_room_open(cur_x - 1, cur_y, task_input):
                    queue.append([cur_step + 1, [cur_x - 1, cur_y]])

        ## checking upper room
        if cur_y > 0:
            if [cur_x, cur_y - 1] not in visited:
                visited.append([cur_x, cur_y - 1])
                if is_room_open(cur_x, cur_y - 1, task_input):
                    queue.append([cur_step + 1, [cur_x, cur_y - 1]])

        ## checking right room
        if [cur_x + 1, cur_y] not in visited:
            visited.append([cur_x + 1, cur_y])
            if is_room_open(cur_x + 1, cur_y, task_input):
                queue.append([cur_step + 1, [cur_x + 1, cur_y]])
        
        ## checking down room
        if [cur_x, cur_y + 1] not in visited:
            visited.append([cur_x, cur_y + 1])
            if is_room_open(cur_x, cur_y + 1, task_input):
                queue.append([cur_step + 1, [cur_x, cur_y + 1]])

        queue.pop(0)

def is_room_open(x, y, inp):
    deci = x*x + 3*x + 2*x*y + y + y*y + inp
    bina = convert_to_binary(deci)
    ones = bina.count("1")
    if ones%2 == 0:
        return True
    else:
        return False

def convert_to_binary(deci):
    if deci < 2:
        return str(deci)
    else:
        return convert_to_binary(int(deci/2)) + str(deci%2)
