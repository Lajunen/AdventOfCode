import readfile

def day12(p):
    data = readfile.read_lines(12)

    ##test_data = ["cpy 41 a","inc a","inc a","dec a","jnz a 2","dec a"]
    ##test_program = compile_program(test_data)

    program = compile_program(data)
    
    if p == 1:
        print("Day 12, Part 1 solution: " + str(bunny_cpu(program, "a", 1)))
    if p == 2:
        print("Day 12, Part 2 solution: " + str(bunny_cpu(program, "a", 2)))


def bunny_cpu(program, value, part):
    mem_reg = {}
    mem_reg["a"] = 0
    mem_reg["b"] = 0
    mem_reg["c"] = 0
    mem_reg["d"] = 0

    if part == 2:
        mem_reg["c"] = 1
    
    line = 0

    while line < len(program):
        if program[line][0] == "cpy":
            if program[line][1].isdigit():
                mem_reg[program[line][2]] = int(program[line][1])
            else:
                mem_reg[program[line][2]] = mem_reg[program[line][1]]
        elif program[line][0] == "inc":
            mem_reg[program[line][1]] += 1
        elif program[line][0] == "dec":
            mem_reg[program[line][1]] -= 1
        elif program[line][0] == "jnz":
            if program[line][1].isdigit():
                if int(program[line][1]) != 0:
                    line += int(program[line][2]) - 1
            else:
                if mem_reg[program[line][1]] != 0:
                    line += int(program[line][2]) - 1

        line += 1
    return mem_reg[value]

def compile_program(data):
    program = []

    for line in data:
        syntax = line.split(" ")
        program.append(syntax)
    
    return program
