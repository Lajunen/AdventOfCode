import readfile
from copy import deepcopy

configurations = []

def day24(p):
    data = readfile.read_lines(24)

    packages = parse_data(data)
    ## test_packages = [1,2,3,4,5,7,8,9,10,11]

    if p == 1:
        print("Day 23, Part 1 solution: " + str(part_one(packages)))
    
    if p == 2:
        print("Day 23, Part 2 solution: " + str(part_two(packages)))

def part_one(packages):
    global configurations
    configuration = [[], [], []]
    packages.sort()
    packages.reverse()
    configuration[0].append(packages[0])

    find_configurations(configuration, packages[1:], 3)

    ideal = [[], [], []]
    for con in configurations:
        ## modifying array to have nested arrays in the right order
        modified = modify_config(deepcopy(con))
        if len(ideal[0]) == 0:
            ideal = deepcopy(modified)
        
        if len(modified[0]) < len(ideal[0]):
            ideal = deepcopy(modified)
        elif len(modified[0]) == len(ideal[0]):
            ## choosing one with lowest saturation
            if calculate_qe(modified[0]) < calculate_qe(ideal[0]):
                ideal = deepcopy(modified)

    return calculate_qe(ideal[0])

def part_two(packages):
    global configurations
    configuration = [[], [], [], []]
    packages.sort()
    packages.reverse()
    configuration[0].append(packages[0])

    find_configurations(configuration, packages[1:], 4)

    ideal = [[], [], [], []]
    for con in configurations:
        print(con)
        ## modifying array to have nested arrays in the right order
        modified = modify_config(deepcopy(con))
        if len(ideal[0]) == 0:
            ideal = deepcopy(modified)
        
        if len(modified[0]) < len(ideal[0]):
            ideal = deepcopy(modified)
        elif len(modified[0]) == len(ideal[0]):
            ## choosing one with lowest saturation
            if calculate_qe(modified[0]) < calculate_qe(ideal[0]):
                ideal = deepcopy(modified)

    return calculate_qe(ideal[0])

def calculate_qe(group):
    prod = 1
    for present in group:
        prod *= present
    
    return prod

def find_configurations(cur_config, packages, groups):
    global configurations

    set_one_full = is_set_full(cur_config, packages, 0)
    set_two_full = is_set_full(cur_config, packages, 1)
    set_three_full = is_set_full(cur_config, packages, 2)

    new_config = deepcopy(cur_config)
    packages_left = deepcopy(packages)

    ## adding to first it fits
    for set_index in range(0, len(new_config), 1):
        ## returning if earlier sets not full
        if set_index > 0 and not set_one_full:
            return
        if set_index > 1 and not set_two_full:
            return
        if set_index > 2 and not set_three_full and groups == 4:
            return

        ## if all but last group is full. adding configuration if not found before
        if groups == 3 and set_index == 2 and set_one_full and set_two_full:
            send_config = deepcopy(cur_config)
            send_config[2] = deepcopy(packages_left)
            modified_config = modify_config(send_config)
            if modified_config not in configurations:
                configurations.append(modified_config)
            return
        elif groups == 4:
            if set_index == 3 and set_one_full and set_two_full and set_three_full:
                send_config = deepcopy(cur_config)
                send_config[3] = deepcopy(packages_left)
                modified_config = modify_config(send_config)
                if modified_config not in configurations:
                    configurations.append(modified_config)
                return

        ## adding package if still dealing with others than last group
        for pack_index in range(0, len(packages_left), 1):
            if groups == 3:
                if (weigh_set(cur_config[0]) + weigh_set(cur_config[1]) + weigh_set(cur_config[2]) + weigh_set(packages_left)) /3 >= weigh_set(cur_config[set_index]) + packages_left[pack_index]:
                    if len(cur_config[set_index]) > 0:
                        if packages_left[pack_index] > cur_config[set_index][-1]:
                            return
                    send_config = deepcopy(cur_config)
                    send_config[set_index].append(packages_left[pack_index])
                    send_packages = deepcopy(packages_left)
                    send_packages.pop(pack_index)
                    find_configurations(send_config, send_packages, groups)
            elif groups == 4:
                if (weigh_set(cur_config[0]) + weigh_set(cur_config[1]) + weigh_set(cur_config[2]) + weigh_set(cur_config[3]) + weigh_set(packages_left)) /4 >= weigh_set(cur_config[set_index]) + packages_left[pack_index]:
                    if len(cur_config[set_index]) > 0:
                        if packages_left[pack_index] > cur_config[set_index][-1]:
                            return
                    send_config = deepcopy(cur_config)
                    send_config[set_index].append(packages_left[pack_index])
                    send_packages = deepcopy(packages_left)
                    send_packages.pop(pack_index)
                    find_configurations(send_config, send_packages, groups)
    return

def is_set_full(config, packages, set_number):
    total_weight = 0
    for set in config:
        total_weight += weigh_set(set)
    total_weight += weigh_set(packages)
    if (total_weight)/len(config) == weigh_set(config[set_number]):
        return True
    return False

def modify_config(config_to_modify):
    modified = []
    cur_config = deepcopy(config_to_modify)
    length_of_longest_array = -1
    for set in cur_config:
        if len(set) > length_of_longest_array or length_of_longest_array == -1:
            length_of_longest_array = len(set)

    ## taking sets in order of length starting with shortest (as santa liked to have room for legs)
    for i in range(0, length_of_longest_array + 1, 1):
        sets_of_current_length = []
        for set in cur_config:
            if len(set) == i:
                new_set = deepcopy(set)
                new_set.sort()
                new_set.reverse()
                sets_of_current_length.append(new_set)
        
        if len(sets_of_current_length) >= 1:
            ## more than one sets of this length, need to sort those
            qe_in_sets = []
            for set in sets_of_current_length:
                qe_in_sets.append(calculate_qe(set))
            
            qe_in_sets.sort()
            for num in qe_in_sets:
                for set in sets_of_current_length:
                    if calculate_qe(set) == num:
                        set_to_add = deepcopy(set)
                        set_to_add.sort()
                        set_to_add.reverse()
                        modified.append(set_to_add)
        elif len(sets_of_current_length) == 1:
            new_set = deepcopy(sets_of_current_length[0])
            new_set.sort()
            new_set.reverse()
            modified.append(new_set)

    return modified

def weight_distributed_correctly(config_to_check):
    if len(config_to_check) == 3:
        if weigh_set(config_to_check[0]) == weigh_set(config_to_check[1]) and weigh_set(config_to_check[1]) == weigh_set(config_to_check[2]):
            return True
    if len(config_to_check) == 4:
        if weigh_set(config_to_check[0]) == weigh_set(config_to_check[1]) and weigh_set(config_to_check[1]) == weigh_set(config_to_check[2]) and weigh_set(config_to_check[2]) == weigh_set(config_to_check[3]):
            return True
    
    return False

## return combined weight of the array (sum of numbers)
def weigh_set(set):
    weight = 0
    for pack in set:
        weight += pack
    
    return weight

## convers strings in array to ints
def parse_data(data):
    packs = []

    for line in data:
        packs.append(int(line))
    
    return packs
