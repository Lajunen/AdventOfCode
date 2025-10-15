highest = 0

def day20(p):
    if p == 1:
        print("Day 20, Part 1 solution: " + str(first_house_to(36000000, 10, 0)))
    
    if p == 2:
        print("Day 20, Part 2 solution: " + str(locate_house(36000000, 11, 50, 100000, 100000)))
        ## print("Day 20, Part 2 solution: " + str(first_house_to(36000000, 11, 50)))

def locate_house(target, value, limit, start, step):
    print("Start: " + str(start) + " step: " + str(step))
    house = start

    while True:
        sum = 0
        for elf in range(limit + 1, 0, -1):
            if house%elf == 0:
                sum += int(value * (house/elf))
        
        if sum >= target:
            if step == 100000:
                step = 50000
                start = int(house/2)
                house = start - step
            elif step == 50000:
                step = 10000
                start = int((house+start)/2)
                house = start - step
            elif step == 10000:
                step = 1000
                start += int((house-start)/5)
                house = start - step
            elif step == 1000:
                step = 100
                start += int((house-start)/5)
                house = start - step
            elif step == 100:
                step = 10
                start += int((house-start)/5)
                house = start - step
            elif step == 10:
                step = 1
                start += int((house-start)/5)
                house = start - step
            elif step == 1:
                break

        house += step
    
    return house

def first_house_to(target, presents_per_elf, house_limit):
    global highest

    house = 1
    goal_not_reached = True
    elves_not_in_game = [0]
    elf_start = 0

    ## setting up some boundaries)

    while goal_not_reached:
        points = 0
        if house < house_limit + 1 or house_limit == 0:
            for i in range(1, house + 1):
                if int(house/i) > house_limit:
                    elf_start = i
                if house%i == 0:
                    points += presents_per_elf*i
        else:
            elf_start = elves_not_in_game[-1] + 1
            for i in range(elf_start, house + 1):
                if int(house/i) > house_limit:
                    elf_start = i
                if house%i == 0 and int(house/i) < house_limit:
                    points += presents_per_elf*i
        if points >= target:
            return house
        house += 1
