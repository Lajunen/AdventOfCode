import readfile

distinct_molecules = []
part_two_steps = 0
start_list = []
work_list = []

## test
stepper = 0

def day19(p):
    possible_subs, target_molecule = parse_data(readfile.read_lines(19))

    global distinct_molecules

    ## test
    ## possible_subs = [["e", "H"], ["e", "O"], ["H", "HO"], ["H", "OH"], ["O", "HH"]]
    ## target_molecule = "HOHOHOHOHO"

    if p == 1:
        part_one(possible_subs, target_molecule)
        print("Day 19, Part 1 solution: " + str(len(distinct_molecules)))
    
    if p == 2:
        part_two(possible_subs, target_molecule, 0)
        check_distinct()
        print("Day 19, Part 2 solution: " + str(part_two_steps))

def check_distinct():
    global distinct_molecules

    for mole in distinct_molecules:
        if distinct_molecules.count(mole) > 1:
            print("warning duplicate found")

def part_one(sublist, target):
    global distinct_molecules
    for sub in sublist:
        if target.count(sub[0]) == 1:
            ## possible sub found only once in the molecule
            if target.replace(sub[0], sub[1]) not in distinct_molecules:
                distinct_molecules.append(target.replace(sub[0], sub[1]))
        if target.count(sub[0]) > 1:
            ## possible sub found more than once in the molecule
            find_multiple_subs(sub, target)

def part_two(sublist, current_molecule, step):
    global part_two_steps

    if part_two_steps != 0 and step >= part_two_steps:
        return

    if current_molecule == "e":
        ## done
        print("Bingo! with " + str(step) + " / lowest: " + str(part_two_steps))
        if part_two_steps != 0:
            if step < part_two_steps:
                print("new lowest steps: " + str(step))
                part_two_steps = step
        else:
            part_two_steps = step
            print("new lowest steps: " + str(step))
        return

    for sub in sublist:
        if sub[1] in current_molecule:
            next_steps = sub_all_two(current_molecule, sub)
            if len(next_steps) > 0:
                for next_step in next_steps:
                    part_two(sublist, next_step, step + 1)
            else:
                return


def sub_all_two(cur, sub):
    global distinct_molecules
    next_steps = []
    for i in range(0, len(cur)-len(sub[1]) + 1):
        if cur[i:i+len(sub[1])] == sub[1]:
            if cur[:i] + sub[0] + cur[i+len(sub[1]):] not in distinct_molecules:
                distinct_molecules.append(cur[:i] + sub[0] + cur[i+len(sub[1]):])
                next_steps.append(cur[:i] + sub[0] + cur[i+len(sub[1]):])
    return next_steps

def part_two_old(sublist, target_molecule, current_molecule):
    global start_list
    global part_two_steps
    global work_list

    compile_starting_list(sublist, target_molecule, current_molecule, 0)
    total_steps = 3

    searching = True
    while searching:
        ## updating start_list
        print("length of priotizable array: " + str(len(work_list)))
        part_two_prioritize(target_molecule)
        print("priotized: current lenghts start: " + str((start_list)) + " and work: " + str(len(work_list)))

        for i in range(0, len(start_list)):
            print("processing " + str(i) + "/" + str(len(start_list)) + ": " + start_list[i])
            process_two_depts(sublist, target_molecule, start_list[i], 0)
        
        total_steps += 2
        if part_two_steps != 0:
            searching = False
    
    return

def part_two_prioritize(tar):
    global work_list
    global start_list

    points = []
    ranking = []

    for i in range(0, len(work_list)):
    ## for step in work_list:
        print("calculating: " + str(i) + "/" + str(len(work_list)))
        points.append([work_list[i], count_match_points_part_two(tar, work_list[i])])
        ranking.append(count_match_points_part_two(tar, work_list[i]))
    
    ranking.sort()
    ranking.reverse()
    ranking = ranking[:100]

    temp_points = []
    for point in points:
        if point[1] >= ranking[-1]:
            temp_points.append(point)
    points = temp_points

    new_step_order = []

    for r in range(0, len(ranking)):
        for s in range(0, len(points)):
            print("processing rank: " + str(r) + "/" + str(len(ranking)) + " points " + str(s) + "/" + str(len(points)))
            if points[s][1] == ranking[r]:
                if points[s][0] not in new_step_order:
                    new_step_order.append(points[s][0])
    print("ranking done")
    print(len(new_step_order))

    if len(new_step_order) > 100:
        start_list = new_step_order[:100]
    else:
        start_list = new_step_order
    work_list = []
    
def process_two_depts(sublist, target_molecule, current_molecule, step):
    global part_two_steps
    global work_list

    ## ending loop conditions
    ## current molecule too long as it can't shrink from substitutes which are of equal length or longer
    if len(current_molecule) > len(target_molecule):
        return
    
    ## target molecule found
    if current_molecule == target_molecule:
        print("bingo!")
        if part_two_steps != 0 and step < part_two_steps:
            part_two_steps = step
        if part_two_steps == 0:
            part_two_steps = step
    
    ## solution has previously been found with fewer steps
    if part_two_steps != 0:
        if step >= part_two_steps:
            return
    
    ## breaking if target molecule and current share under 20% matching characters when current molecule is already 15+ characters long
    if len(current_molecule) >= 10 and len(current_molecule) <= 20:
        if int((count_match_points(target_molecule, current_molecule) * 100) / len(current_molecule)) < 20:
            return
    
    if len(current_molecule) >= 21 and len(current_molecule) <= 40:
        if int((count_match_points(target_molecule, current_molecule) * 100) / len(current_molecule)) < 40:
            return
    
    if len(current_molecule) >= 41 and len(current_molecule) < 60:
        if int((count_match_points(target_molecule, current_molecule) * 100) / len(current_molecule)) < 60:
            return

    if len(current_molecule) >= 61:
        if int((count_match_points(target_molecule, current_molecule) * 100) / len(current_molecule)) < 80:
            return
        else:
            ## test
            print("current: " + current_molecule + " (" + str(int((count_match_points(target_molecule, current_molecule) * 100) / len(current_molecule))) + "%)")

    ## doing the possible substitutes
    for sub in sublist:
        if sub[0] in current_molecule:
            ## only checking if something can be substituted
            possible_next_steps = sub_all(target_molecule, current_molecule, sub)
            
            if len(possible_next_steps) > 0:
                for check_next in possible_next_steps:
                    if step == 2:
                        work_list.append(check_next)
                    else:
                        if count_match_points_part_two(target_molecule, check_next) >= count_match_points_part_two(target_molecule, current_molecule):
                            process_two_depts(sublist, target_molecule, check_next, step + 1)

def compile_starting_list(sublist, target_molecule, current_molecule, depth):
    global work_list

    ## trying to compile a list of all first 3 substitutions
    for sub in sublist:
        if sub[0] in current_molecule:
            possible_next_steps = sub_all(target_molecule, current_molecule, sub)

            if len(possible_next_steps) > 0:
                if depth == 3:
                    for next_step in possible_next_steps:
                        if next_step not in work_list and count_match_points_part_two(target_molecule, next_step) >= count_match_points_part_two(target_molecule, current_molecule):
                            work_list.append(next_step)
                    return
                for check_next in possible_next_steps:
                    compile_starting_list(sublist, target_molecule, check_next, depth + 1)
    
    return

def sub_all(tar, cur, sub):
    global distinct_molecules
    next_steps = []
    for i in range(0, len(cur)-len(sub[0]) + 1):
        if cur[i:i+len(sub[0])] == sub[0] and len(cur[:i] + sub[1] + cur[i+len(sub[0]):]) <= len(tar):
            if cur[:i] + sub[1] + cur[i+len(sub[0]):] not in distinct_molecules:
                next_steps.append(cur[:i] + sub[1] + cur[i+len(sub[0]):])
                distinct_molecules.append(cur[:i] + sub[1] + cur[i+len(sub[0]):])

    prioritized_steps = prioritize_next_steps(tar, cur, next_steps)
    return prioritized_steps

def prioritize_next_steps(tar, cur, next_steps):
    ## quick priotize based on how many first characters match
    points = []
    ranking = []

    for step in next_steps:
        cur_points = 0
        for i in range(len(step)):
            cur_points += count_match_points(tar, step)
        points.append([step, cur_points])
        ranking.append(cur_points)
    
    ranking.sort()
    ranking.reverse()

    prioritized_steps = []

    for rank in ranking:
        for step_point in points:
            if step_point[1] == rank:
                prioritized_steps.append(step_point[0])
    
    return prioritized_steps

def count_match_points_part_two(tar, mole):
    points = 0
    for i in range(0, len(mole)):
        if tar[i] == mole[i]:
            ## awarding more points for hits earlier in the molecule
            points += len(mole)-i

    return points

def count_match_points(tar, mole):
    points = 0
    for i in range(0, len(mole)):
        if tar[i] == mole[i]:
            points += 1
    
    return points

def find_multiple_subs(sub, target):
    global distinct_molecules

    for i in range(0, len(target)-len(sub[0]) + 1):
        if target[i:i+len(sub[0])] == sub[0]:
            if target[:i] + sub[1] + target[i+len(sub[0]):] not in distinct_molecules:
                distinct_molecules.append(target[:i] + sub[1] + target[i+len(sub[0]):])
            
def parse_data(data):
    subs = []
    target = ""
    for line in data:
        if " => " in line:
            bits = line.split(" => ")
            new_sub = [bits[0], bits[1]]
            subs.append(new_sub)
        if " => " not in line and len(line) > 0:
            target = line

    return subs, target

day19(2)