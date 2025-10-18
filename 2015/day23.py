import readfile

def day23(p):
    program = readfile.read_lines(23)

    memory_state = cpu_emulator(program, p)

    if p == 1:
        print("Day 23, Part 1 solution: " + str(memory_state["b"]))
    if p == 2:
        print("Day 23, Part 2 solution: " + str(memory_state["b"]))

def cpu_emulator(prog, part):
    mem_registry = reset_memory()
    if part == 2:
        mem_registry["a"] = 1

    current_line = 0

    while current_line < len(prog):
        ## exits if trying to access line before first line
        if current_line < 0:
            return mem_registry
        
        syntax = compile_line(prog[current_line])
    
        if syntax[0] == "hlf":
            mem_registry[syntax[1]] = int(mem_registry[syntax[1]]) / 2
        elif syntax[0] == "tpl":
            mem_registry[syntax[1]] = int(mem_registry[syntax[1]]) * 3
        elif syntax[0] == "inc":
            mem_registry[syntax[1]] = int(mem_registry[syntax[1]]) + 1
        elif syntax[0] == "jmp":
            current_line = current_line + int(syntax[1]) - 1
        elif syntax[0] == "jie":
            if mem_registry[syntax[1]]%2 == 0:
                current_line = current_line + int(syntax[2]) - 1
        elif syntax[0] == "jio":
            if mem_registry[syntax[1]] == 1:
                current_line = current_line + int(syntax[2]) - 1

        current_line += 1
    
    return mem_registry

def reset_memory():
    mem_reg = {}
    mem_reg["a"] = 0
    mem_reg["b"] = 0

    return mem_reg

def compile_line(syntax_line):
    syntax_line = syntax_line.replace(",", "")

    compiled_syntax = syntax_line.split(" ")

    return compiled_syntax
