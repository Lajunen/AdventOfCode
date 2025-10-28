import readfile
from copy import deepcopy
import os

def day11(p):
    global fastest

    data = readfile.read_lines(11)

    initial_condition = get_initial_condition(data, p)
    

    if p == 1:
        ## solve_puzzle(initial_condition, 0, -1)
        print("Day 11, Part 1 solution: " + str(bfs_solve_puzzle(initial_condition)))
    
    if p == 2:
        print("Day 11, Part 2 solution: " + str(bfs_solve_puzzle(initial_condition)))


## BFS solve ##
def bfs_solve_puzzle(state):
    queue = []
    visited_states = []

    queue.append([0, deepcopy(state)])
    visited_states.append([0, deepcopy(state)])

    while len(queue) >= 1:
        show_state(queue[0][1])

        ## moving items
        for first_item in queue[0][1]:
            if first_item.name != "ME" and first_item.floor == find_my_floor(queue[0][1]):
                ## moving item as single first
                if find_my_floor(queue[0][1]) < 4:
                    new_state = move_item_to_floor(first_item.name, 1, queue[0][1])
                    if is_solved(new_state):
                        return queue[0][0] + 1
                    if not microchip_burned(new_state):
                        if is_unique(new_state, queue):
                            if len(visited_states) > 0:
                                if is_unique(new_state, visited_states):
                                    ## here additional checks for single item moving up
                                    queue.append([queue[0][0] + 1, deepcopy(new_state)])
                if find_my_floor(queue[0][1]) > 1:
                    new_state = move_item_to_floor(first_item.name, -1, queue[0][1])
                    if is_solved(new_state):
                        return queue[0][0] + 1
                    if not microchip_burned(new_state):
                        if is_unique(new_state, queue):
                            if len(visited_states) > 0:
                                if is_unique(new_state, visited_states):
                                    ## here additional checks for single item moving down
                                    queue.append([queue[0][0] + 1, deepcopy(new_state)])

                ## adding second item
                for second_item in queue[0][1]:
                    if second_item.name != "ME" and second_item.name != first_item.name and second_item.floor == find_my_floor(queue[0][1]):
                        if find_my_floor(queue[0][1]) < 4:
                            new_state = move_two_items_to_floor(first_item.name, second_item.name, 1, queue[0][1])
                            if is_solved(new_state):
                                return queue[0][0] + 1
                            if not microchip_burned(new_state):
                                if is_unique(new_state, queue):
                                    if len(visited_states) > 0:
                                        if is_unique(new_state, visited_states):
                                            ## here can be added other checks too
                                            queue.append([queue[0][0] + 1, deepcopy(new_state)])
                        if find_my_floor(queue[0][1]) > 1:
                            new_state = move_two_items_to_floor(first_item.name, second_item.name, -1, queue[0][1])
                            if is_solved(new_state):
                                return queue[0][0] + 1
                            if not microchip_burned(new_state):
                                if is_unique(new_state, queue):
                                    if len(visited_states) > 0:
                                        if is_unique(new_state, visited_states):
                                            ## here can be added other checks too
                                            queue.append([queue[0][0] + 1, deepcopy(new_state)])
        visited_states.append(deepcopy(queue[0]))
        while visited_states[0][0] + 3 <= visited_states[-1][0]:
            visited_states.pop(0)
        queue.pop(0)    

## checks if similar state already in queue
def is_unique(state, queue):
    state_map = map_state(state)
    state_map.sort()

    for que in queue:
        que_map = map_state(que[1])
        que_map.sort()
        if state_map == que_map and find_my_floor(state) == find_my_floor(que[1]):
            return False
    return True

## converts visual state info to easy to compare array of tuplees
def map_state(state):
    mapped = []
    for item_to_map in state:
        if item_to_map.name[1] == "M":
            for item_to_pair in state:
                if item_to_pair.name[0] == item_to_map.name[0] and item_to_pair.name[1] == "G":
                    mapped.append((item_to_map.floor, item_to_pair.floor))
    
    return mapped

## moves two items to target floor
def move_two_items_to_floor(item1, item2, amount, state):
    new_state = deepcopy(state)

    my_floor = find_my_floor(new_state)

    new_state = deepcopy(change_item_floor(new_state, item1, amount))
    new_state = deepcopy(change_item_floor(new_state, item2, amount))
    new_state = deepcopy(change_item_floor(new_state, "ME", amount))

    return new_state

## moves item to target floor
def move_item_to_floor(item_to_move, amount, state):
    new_state = deepcopy(state)

    my_floor = find_my_floor(new_state)

    new_state = deepcopy(change_item_floor(new_state, item_to_move, amount))
    new_state = deepcopy(change_item_floor(new_state, "ME", amount))
    
    return new_state

## moves item in state one floor up or down and returns new state
def change_item_floor(state, item_to_move, floor):
    new_state = deepcopy(state)

    for new_item in new_state:
        if new_item.name == item_to_move:
            new_item.change_floor(floor)
    
    return new_state

## returns my floor
def find_my_floor(state):
    for cur_item in state:
        if cur_item.name == "ME":
            return cur_item.floor
    
    return 0

## returns true if all items are at the floor number 4
def is_solved(state):
    for cur_item in state:
        if cur_item.floor != 4:
            return False
    
    return True

## returns true if current state burns any microchips
def microchip_burned(state):
    for floor in range(1, 5, 1):
        for item1 in state:
            if item1.name[1] == "M" and item1.floor == floor:
                chip_burned = False
                chip_safe = False
                for item2 in state:
                    if item2.name[1] == "G" and item2.floor == floor:
                        if item1.name[0] == item2.name[0]:
                            chip_safe = True
                        else:
                            chip_burned = True
                if chip_burned and not chip_safe:
                    return True
    
    return False

## prints a visual image of state
def show_state(state):
    os.system('clear')
    for i in range(4, 0, -1):
        floor_info = "F" + str(i) + " | .. | .. | .. | .. | .. | .. | .. | .. | .. | .. | .. | .. | .. | .. | .. |"
        for cur_item in state:
            if cur_item.floor == i:
                offset = 0
                if cur_item.name[1] == "G":
                    offset = 1
                if cur_item.name[0] == "R":
                    floor_info = floor_info[:10 + offset*5] + cur_item.name + floor_info[12 + offset*5:]
                elif cur_item.name[0] == "S":
                    floor_info = floor_info[:20 + offset*5] + cur_item.name + floor_info[22 + offset*5:]
                elif cur_item.name[0] == "C":
                    floor_info = floor_info[:30 + offset*5] + cur_item.name + floor_info[32 + offset*5:]
                elif cur_item.name[0] == "T":
                    floor_info = floor_info[:40 + offset*5] + cur_item.name + floor_info[42 + offset*5:]
                elif cur_item.name[0] == "P":
                    floor_info = floor_info[:50 + offset*5] + cur_item.name + floor_info[52 + offset*5:]
                elif cur_item.name[0] == "D":
                    floor_info = floor_info[:60 + offset*5] + cur_item.name + floor_info[62 + offset*5:]
                elif cur_item.name[0] == "E":
                    floor_info = floor_info[:70 + offset*5] + cur_item.name + floor_info[72 + offset*5:]
                if cur_item.name == "ME":
                    floor_info = floor_info[:5] + "ME" + floor_info[7:]

        print(floor_info)

## gets initial state from input text, adds part 2 stuff if needed
def get_initial_condition(data, part):
    state = []

    for line in data:
        line = line.replace(".", "")
        line = line.replace(",", "")
        parts = line.split(" ")

        ## taking the floor
        floor = 0
        if parts[1] == "first":
            floor = 1
        elif parts[1] == "second":
            floor = 2
        elif parts[1] == "third":
            floor = 3
        elif parts[1] == "fourts":
            floor = 4

        ## taking the items on the floor
        for i in range(0, len(parts), 1):
            if parts[i] == "generator":
                new_item = item(parts[i-1][0].upper() + parts[i][0].upper(), floor)
                state.append(deepcopy(new_item))
            if parts[i] == "microchip":
                chip_parts = parts[i-1].split("-")
                new_item = item(chip_parts[0][0].upper() + parts[i][0].upper(), floor)
                state.append(deepcopy(new_item))
    
    if part == 2:
        ## adding part 2 items
        new_item = item("EG", 1)
        state.append(deepcopy(new_item))
        new_item = item("EM", 1)
        state.append(deepcopy(new_item))
        new_item = item("DG", 1)
        state.append(deepcopy(new_item))
        new_item = item("DM", 1)
        state.append(deepcopy(new_item))

    ## finally adding me
    new_item = item("ME", 1)
    state.append(deepcopy(new_item))
    return state

## created a class instead of array to help with readability
class item:
    name = ""
    floor = 0

    def __init__(self, name, floor):
        self.name = name
        self.floor = floor
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return str(self.name)
    
    def change_floor(self, amount):
        self.floor += amount
