def day10(p):
    input = "1113122113"

    if p == 1:
        print("Day 10, Part 1 solution: " + str(play_game(input, 40)))
    
    if p == 2:
        print("Day 10, Part 2 solution: " + str(play_game(input, 50)))


def play_game(input, rounds):
    for round in range(rounds):
        input = play_round(input)

    return len(input)    

def play_round(input):
    i = 0
    cur_num = ""
    cur_cnt = 0

    result = ""

    while i < len(input):
        if cur_num == "":
            cur_num = input[i]

        if cur_num == input[i]: 
            cur_cnt += 1
        
        if cur_num != input[i]:
            result += str(cur_cnt)
            result += cur_num
            cur_num = input[i]
            cur_cnt = 1
        
        if i == len(input)-1:
            result += str(cur_cnt)
            result += cur_num
                
        i += 1
    
    return result
