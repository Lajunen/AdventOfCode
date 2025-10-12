import readfile
def day07(p):
    operations = readfile.read_lines(7)

    if p == 1:
        print("Day 7, Part 1 solution: " + str(part_one(operations)))
    
    if p == 2:
        print("Day 7, Part 2 solution: " + str(part_two(operations)))

def part_one(ops):
    values = {}
    values_found = 0
    
    ## main loop to run through while operations left
    while len(ops) > 0:
        ## going through each operation
        for op in ops:
            cur_op = op.split(" -> ")
            ## [0] should now hold either number value or formula with NOT, AND, OR, RSHIFT, LSHIFT
            if cur_op[1] not in values:
                if "NOT" in cur_op[0]:
                    ## format: NOT var // variable can be number too
                    vari = cur_op[0][4:]
                    if vari.isnumeric():
                        ## we have a numerical value
                        bits = num_to_bin(vari)

                        result = not_gate(bits)

                        value = bin_to_num(result)

                        values[cur_op[1]] = value
                    else:
                        ## we have variable
                        if vari in values:
                            bits = num_to_bin(values[vari])

                            result = not_gate(bits)

                            value = bin_to_num(result)

                            values[cur_op[1]] = value

                if "AND" in cur_op[0]:
                    ## format: var AND var // variables can be numbers too
                    unknown_variables = False
                    varies = cur_op[0].split(" AND ")
                    if varies[0].isnumeric():
                        var1 = num_to_bin(varies[0])
                    else:
                        if varies[0] in values:
                            var1 = num_to_bin(values[varies[0]])
                        else:
                            unknown_variables = True
                    
                    if varies[1].isnumeric():
                        var2 = num_to_bin(varies[1])
                    else:
                        if varies[1] in values:
                            var2 = num_to_bin(values[varies[1]])
                        else:
                            unknown_variables = True
                    
                    if not unknown_variables:
                        result = and_gate(var1, var2)

                        value = bin_to_num(result)

                        values[cur_op[1]] = value

                if "OR" in cur_op[0]:
                    ## format: var OR var // variables can be numbers too
                    varies = cur_op[0].split(" OR ")
                    unknown_variables = False
                    if varies[0].isnumeric():
                        var1 = num_to_bin(varies[0])
                    else:
                        if varies[0] in values:
                            var1 = num_to_bin(values[varies[0]])
                        else:
                            unknown_variables = True
                    
                    if varies[1].isnumeric():
                        var2 = num_to_bin(varies[1])
                    else:
                        if varies[1] in values:
                            var2 = num_to_bin(values[varies[1]])
                        else:
                            unknown_variables = True
                    
                    if not unknown_variables:
                        result = or_gate(var1, var2)

                        value = bin_to_num(result)

                        values[cur_op[1]] = value

                if "RSHIFT" in cur_op[0]:
                    ## format: var RSHIFT number // variable can be number too
                    varis = cur_op[0].split(" RSHIFT ")
                    if varis[0].isnumeric():
                        bits = num_to_bin(varis[0])

                        for i in range (0, int(varis[1])):
                            bits = rshift_gate(bits)

                        value = bin_to_num(bits)

                        values[cur_op[1]] = value
                    else:
                        if varis[0] in values:
                            bits = num_to_bin(values[varis[0]])

                            for i in range(0, int(varis[1])):
                                bits = rshift_gate(bits)

                            value = bin_to_num(bits)

                            values[cur_op[1]] = value

                if "LSHIFT" in cur_op[0]:
                    ## format: var LSHIFT number // variable can be number too
                    varis = cur_op[0].split(" LSHIFT ")
                    if varis[0].isnumeric():
                        bits = num_to_bin(varis[0])

                        for i in range(0, int(varis[1])):
                            bits = lshift_gate(bits)

                        value = bin_to_num(bits)

                        values[cur_op[1]] = value
                    else:
                        if varis[0] in values:
                            bits = num_to_bin(values[varis[0]])

                            for i in range(0, int(varis[1])):
                                bits = lshift_gate(bits)

                            value = bin_to_num(bits)

                            values[cur_op[1]] = value

                if len(cur_op[0].split(" ")) == 1:
                    ## format: var or direct value
                    if cur_op[0].isnumeric():
                        values[cur_op[1]] = int(cur_op[0])
                    else:
                        if cur_op[0] in values:
                            values[cur_op[1]] = values[cur_op[0]]

        ## checking if any operations succesfully completed
        if values_found == len(values):
            break
        else:
            values_found = len(values)

    return values["a"]

def part_two(ops):
    new_ops = []

    for op in ops:
        op_info = op.split(" -> ")
        if op_info[1] == "b":
            new_ops.append("16076 -> b")
        else:
            new_ops.append(op)
    
    return part_one(new_ops)

def num_to_bin(s):
    bin = ""
    num = int(s)

    if num >= 32768:
        bin += "1"
        num -= 32768
    else:
        bin += "0"

    if num >= 16384:
        bin += "1"
        num -= 16384
    else:
        bin += "0"
    
    if num >= 8192:
        bin += "1"
        num -= 8192
    else:
        bin += "0"
    
    if num >= 4096:
        bin += "1"
        num -= 4096
    else:
        bin += "0"
    
    if num >= 2048:
        bin += "1"
        num -= 2048
    else:
        bin += "0"
    
    if num >= 1024:
        bin += "1"
        num -= 1024
    else:
        bin += "0"
    
    if num >= 512:
        bin += "1"
        num -= 512
    else:
        bin += "0"

    if num >= 256:
        bin += "1"
        num -= 256
    else:
        bin += "0"

    if num >= 128:
        bin += "1"
        num -= 128
    else:
        bin += "0"

    if num >= 64:
        bin += "1"
        num -= 64
    else:
        bin += "0"

    if num >= 32:
        bin += "1"
        num -= 32
    else:
        bin += "0"

    if num >= 16:
        bin += "1"
        num -= 16
    else:
        bin += "0"

    if num >= 8:
        bin += "1"
        num -= 8
    else:
        bin += "0"

    if num >= 4:
        bin += "1"
        num -= 4
    else:
        bin += "0"

    if num >= 2:
        bin += "1"
        num -= 2
    else:
        bin += "0"

    if num == 1:
        bin += "1"
    else:
        bin += "0"

    return bin

def bin_to_num(s):
    value = 32768 * int(s[0]) + 16384  * int(s[1]) + 8192 * int(s[2]) + 4096 * int(s[3])
    value += 2048 * int(s[4]) + 1024 * int(s[5]) + 512 * int(s[6]) + 256 * int(s[7])
    value += 128 * int(s[8]) + 64 * int(s[9]) + 32 * int(s[10]) + 16 * int(s[11])
    value += 8 * int(s[12]) + 4 * int(s[13]) + 2 * int(s[14]) + int(s[15])

    return value

def not_gate(s):
    res = ""

    for bit in s:
        if bit == "0":
            res += "1"
        else:
            res += "0"
    
    return res

def and_gate(s1, s2):
    res = ""
    for i in range(0, 16):
        if s1[i] == "1" and s2[i] == "1":
            res += "1"
        else:
            res += "0"
    
    return res

def or_gate(s1, s2):
    res = ""
    for i in range(0, 16):
        if s1[i] == "1" or s2[i] == "1":
            res += "1"
        else:
            res += "0"
    
    return res

def rshift_gate(s1):
    res = "0" + s1[:15]
    return res

def lshift_gate(s1):
    res = s1[1:] + "0"
    return res

