import readfile

solutions = 0
min_containers = 0

def day17(p):
    data = readfile.read_lines(17)

    containers = parse_data(data)

    global solutions
    global min_containers

    if p == 1:
        find_combinations(containers, 150, 1, 0)
        print("Day 17, Part 1 solution: " + str(solutions))
    
    if p == 2:
        min_containers = len(containers)
        find_combinations(containers, 150, 2, 0)
        print("Day 17, Part 2 solution: " + str(solutions))

        

def find_combinations(containers, eggnog, part, containers_used):
    global solutions
    global min_containers

    if eggnog == 0:
        if part == 1:
            solutions += 1
        if part == 2:
            if containers_used == min_containers:
                solutions += 1
            if containers_used < min_containers:
                solutions = 1
                min_containers = containers_used

        return
    else:
        ## eggnog left
        for con in range(0, len(containers)):
            if containers[con] <= eggnog:
                ## enough eggnog left to fill current container
                if con < len(containers) - 1:
                    ## containers left after this
                    find_combinations(containers[con + 1:], eggnog - containers[con], part, containers_used + 1)
                else:
                    ## last container
                    if containers[con] == eggnog:
                        ## finishes correctly
                        if part == 1:
                            solutions += 1
                        if part == 2:
                            if containers_used + 1 == min_containers:
                                solutions += 1
                            if containers_used + 1 < min_containers:
                                solutions = 1
                                min_containers = containers_used + 1
                    return

def parse_data(data):
    containers = []

    for line in data:
        containers.append(int(line))
    
    containers.sort()
    containers.reverse()

    return containers