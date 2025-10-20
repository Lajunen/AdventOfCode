import readfile

def day07(p):
    ips = readfile.read_lines(7)

    if p == 1:
        print("Day 7, Part 1 solution: " + str(part_one(ips)))
    if p == 2:
        print("Day 7, Part 2 solution: " + str(part_two(ips)))

def part_one(ips):
    supports = 0
    for ip in ips:
        if supports_tls(ip):
            supports += 1
    
    return supports

def part_two(ips):
    supports = 0
    for ip in ips:
        if supports_ssl(ip):
            supports += 1
    
    return supports

def supports_ssl(ip):
    aba_outs = []
    aba_ins = []
    in_brackets = False
    index = 0

    while index < len(ip) - 2:
        if ip[index] == "[":
            in_brackets = True
        elif ip[index] == "]":
            in_brackets = False
        else:
            ch_one = ip[index]
            if ip[index + 1] != "[" and ip[index + 1] != "]" and ip[index + 1] != ch_one:
                ch_two = ip[index + 1]
                if ip[index + 2] == ch_one:
                    if in_brackets:
                        aba_ins.append(ip[index:index + 3])
                    else:
                        aba_outs.append(ip[index:index + 3])
        index += 1

    if len(aba_ins) > 0 or len(aba_outs) > 0:
        for out_side in aba_outs:
            corresponding = out_side[1:2] + out_side[0:1] + out_side[1:2]
            if corresponding in aba_ins:
                return True

    return False
        
def supports_tls(ip):
    abba_out = False
    abba_in = False
    in_brackets = False
    index = 0

    while index < len(ip) - 3:
        if ip[index] == "[":
            in_brackets = True
        elif ip[index] == "]":
            in_brackets = False
        else:
            ch_one = ip[index]
            if ip[index + 1] != "[" and ip[index + 1] != "]" and ip[index + 1] != ch_one:
                ch_two = ip[index + 1]
                if ip[index + 2] == ch_two and ip[index + 3] == ch_one:
                    if in_brackets:
                        abba_in = True
                    else:
                        abba_out = True
                    index += 3
        index += 1
    if abba_out and not abba_in:
        return True
    else:
        return False
