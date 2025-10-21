import readfile

def day09(p):
    data = readfile.read_line(9)

    if p == 1:
        print("Day 9, Part 1 solution: " + str(part_one(data)))
    if p == 2:
        print("Day 9, Part 2 solution: " + str(part_two(data)))

def part_one(data):
    length = 0
    index = 0

    while index < len(data):
        if data[index] == "(":
            ## start of marker
            marker_end_index = index
            end_found = False
            while not end_found:
                marker_end_index += 1
                if data[marker_end_index] == ")":
                    ## marker end index found
                    end_found = True
            marker_info = extract_marker_info(data[index:marker_end_index + 1])
            marker_data_length = len(data[marker_end_index + 1:marker_end_index + 1 + marker_info[0]])
            length += marker_data_length*marker_info[1]
            index = marker_end_index + marker_info[0]
        else:
            length += 1
        
        index += 1
    
    return length

def part_two(data):
    length = 0
    index = 0

    while index < len(data):
        if data[index] == "(":
            ## start of marker
            marker_end_index = index
            end_found = False
            while not end_found:
                marker_end_index += 1
                if data[marker_end_index] == ")":
                    ## marker end index found
                    end_found = True
            marker_info = extract_marker_info(data[index:marker_end_index + 1])
            marker_data = data[marker_end_index + 1:marker_end_index + 1 + marker_info[0]]
            if "(" in marker_data:
                marker_length = get_length(marker_data)
            else:
                marker_length = len(marker_data)
            length += marker_length*marker_info[1]
            index = marker_end_index + marker_info[0]
        else:
            length += 1
        
        index += 1
    
    return length

def get_length(data):
    decompressed_length = 0
    index = 0
    while index < len(data):
        if data[index] == "(":
            ## start of marker
            marker_end_index = index
            end_found = False
            while not end_found:
                marker_end_index += 1
                if data[marker_end_index] == ")":
                    ## marker end index found
                    end_found = True
            marker_info = extract_marker_info(data[index:marker_end_index + 1])
            marker_data = data[marker_end_index + 1:marker_end_index + 1 + marker_info[0]]
            if "(" in marker_data:
                marker_length = get_length(marker_data)
            else:
                marker_length = len(marker_data)
            decompressed_length += marker_length*marker_info[1]
            index = marker_end_index + marker_info[0]
        else:
            decompressed_length += 1
            
        index += 1
    
    return decompressed_length
    
def extract_marker_info(marker):
    info = marker[1:len(marker)-1]
    bits = info.split("x")
    return [int(bits[0]), int(bits[1])]
