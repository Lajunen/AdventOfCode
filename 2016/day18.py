import readfile

def day18(p):
    inp = readfile.read_line(18)
    test_inp = ".^^.^.^^^^"

    if p == 1:
        print("Day 18, Part 1 solution: " + str(count_safe_rooms(inp, 0, 40)))
    if p == 2:
        print("Day 18, Part 2 solution: " + str(count_safe_rooms(inp, 0, 400000)))

def count_safe_rooms(last_row, safe_rooms, target_row):
    ## adding safe rooms from first row
    for ch in last_row:
        if ch == ".":
            safe_rooms += 1
    
    for row in range(0, target_row - 1, 1):
        next_row = ""
        for col in range(0, len(last_row), 1):
            ## look previous rooms left (lc), center (cc), right(rc) and marking if trapped
            ## left room
            if col == 0:
                lc = False
            else:
                if last_row[col - 1] == "^":
                    lc = True
                else:
                    lc = False
            ## center room
            if last_row[col] == "^":
                cc = True
            else:
                cc = False
            ## right room
            if col == len(last_row) - 1:
                rc = False
            else:
                if last_row[col + 1] == "^":
                    rc = True
                else:
                    rc = False
            
            ## adding current room
            if (lc and cc and not rc) or (cc and rc and not lc) or (not lc and not cc and rc) or (lc and not cc and not rc):
                next_row += "^"
            else:
                next_row += "."

        for ch in next_row:
            if ch == ".":
                safe_rooms += 1
        
        last_row = next_row

    return safe_rooms
               
        

day18(2)