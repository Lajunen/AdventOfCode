import readfile
from copy import deepcopy

p_one_answer = ""
p_two_answer = 1

def day10(p):
    input = readfile.read_lines(10)
    bots = []
    outputs = []

    part_one_and_two(input, bots, outputs, p)
    if p == 1:
        print("Day 10, Part 1 solution: " + p_one_answer)
    if p == 2:
        print("Day 10, Part 2 solution: " + str(p_two_answer))
    ## operate_input(test_input, bots, outputs)

def part_one_and_two(input, bots, outputs, part):
    inputs_left = []
    values_left = []
    for line in input:
        if "value" in line:
            values_left.append(line)
        else:
            inputs_left.append(line)
    
    new_bots = operate_value_inputs(values_left)
    operate_robot_inputs(inputs_left, new_bots, outputs, part)

def operate_value_inputs(inputs):
    new_bots = []

    for line in inputs:
            value, target = get_value_info(line)
            target_found = False
            for cur_bot in new_bots:
                if cur_bot.name == target[1] and target[0] == "bot":
                    cur_bot.get_chip(value)
                    target_found = True
            if not target_found:
                if target[0] == "bot":
                    new_bot = bot(target[1])
                    new_bot.get_chip(value)
                    new_bots.append(deepcopy(new_bot))
    
    return deepcopy(new_bots)

def operate_robot_inputs(input, bots, outputs, part):
    index = 0
    while len(input) > 0:
        line = input[index]
        actbot, low_target, high_target = get_action_info(line)
        giver_can_act = False
        low_val = 0
        high_val = 0
        for giver in bots:
            if giver.name == actbot:
                if giver.ready_to_act():
                    low_val = giver.give_low()
                    high_val = giver.give_high()
                    if low_val == 17 and high_val == 61:
                        if part == 1:
                            global p_one_answer
                            p_one_answer = giver.name
                    giver_can_act = True

        if giver_can_act:
            getter_found = False
            if low_target[0] == "bot":
                for getter in bots:
                    if getter.name == low_target[1]:
                        getter.get_chip(low_val)
                        getter_found = True
                if not getter_found:
                    new_bot = bot(low_target[1])
                    new_bot.get_chip(low_val)
                    bots.append(deepcopy(new_bot))
            elif low_target[0] == "output":
                for bin in outputs:
                    if bin.name == low_target[1]:
                        bin.get_chip(low_val)
                if not getter_found:
                    new_bin = output(low_target[1])
                    new_bin.get_chip(low_val)
                    outputs.append(deepcopy(new_bin))
            getter_found = False
            if high_target[0] == "bot":
                for getter in bots:
                    if getter.name == high_target[1]:
                        getter.get_chip(high_val)
                        getter_found = True
                if not getter_found:
                    new_bot = bot(high_target[1])
                    new_bot.get_chip(high_val)
                    bots.append(deepcopy(new_bot))
            elif high_target[0] == "output":
                for bin in outputs:
                    if bin.name == high_target[1]:
                        bin.get_chip(high_val)
                if not getter_found:
                    new_bin = output(high_target[1])
                    new_bin.get_chip(high_val)
                    outputs.append(deepcopy(new_bin))
            input.pop(index)

        if index > len(input) - 2:
            index = 0
        else:
            index += 1
        
    if part == 2:
        global p_two_answer
        for outp in outputs:
            if outp.name == "0" or outp.name == "1" or outp.name == "2":
                p_two_answer *= outp.chips[0]
    return

def get_action_info(line):
    bits = line.split(" ")
    return bits[1], [bits[5], bits[6]], [bits[10], bits[11]]

def get_value_info(line):
    bits = line.split(" ")
    return int(bits[1]), [bits[4], bits[5]]

class output:
    chips = []

    def __init__(self, name):
        self.name = name
        self.chips = []
    
    def get_chip(self, value):
        self.chips.append(value)

class bot:

    def __init__(self, name):
        self.name = name
        self.chips = [-1, -1]

    def __str__(self):
        return "Name: " + self.name + " chips: " + str(self.chips[0]) + " and " + str(self.chips[1])
 
    def get_chip(self, value):
        inserted = False
        for i in range(0, 2, 1):
            if self.chips[i] == -1 and not inserted:
                self.chips[i] = value
                inserted = True
    
    def give_low(self):
        self.chips.sort()
        if self.chips[0] == -1:
            val = self.chips[1]
            self.chips[1] = -1
        else:
            val = self.chips[0]
            self.chips[0] = -1
        return val
    
    def give_high(self):
        self.chips.sort()
        if self.chips[1] == -1:
            val = self.chips[0]
            self.chips[0] = -1
        else:
            val = self.chips[1]
            self.chips[1] = -1
        return val
    
    def ready_to_act(self):
        for chip in self.chips:
            if chip == -1:
                return False
        return True

day10(2)