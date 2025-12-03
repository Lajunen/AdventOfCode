import hashlib
from copy import deepcopy

def day14(p):
    inp = "cuanljph"
    tmp_inp = "abc"

    if p == 1:
        print("Day 14, Part 1 solution: " + str(generate_keys(inp, 64, 1)))
    if p == 2:
        print("Day 14, Part 2 solution: " + str(generate_keys(inp, 64, 2)))

def generate_keys(inp, amount, part):
    index = 0
    
    trips_found = []
    keys = []
    breakout = 0

    while True:
        if part == 1:
            hashed = hashlib.md5((inp + str(index)).encode()).hexdigest().lower()
        if part == 2:
            hashed = hashlib.md5((inp + str(index)).encode()).hexdigest().lower()
            for i in range(0, 2016, 1):
                hashed = hashlib.md5(hashed.encode()).hexdigest().lower()

        trips, fives = examine_hash(hashed, index)

        if trips != "":
            trips_found.append(deepcopy([index, trips]))

        if fives != "":
            for trip in trips_found:
                if len(fives) > 1:
                    print("multiple fives!")
                for cha in fives:
                    if trip[1] == cha and index - trip[0] <= 1001 and trip[0] != index:
                        keys.append(deepcopy(trip[0]))
                        if len(keys) == amount:
                            breakout = index + 1000

        if breakout > 0 and breakout < index:
            keys = list(set(keys))
            keys.sort()
            print(str(keys))
            return keys[amount-1]
        
        index += 1

def examine_hash(s, index):
    consecs = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
            if i == len(s) - 1:
                consecs.append(s[i-1]*count)
        else:
            consecs.append(s[i-1]*count)
            count = 1
    trips = ""
    fives = ""
    if index == 22551:
        print(s)
    for cons in consecs:
        if len(cons) == 3 or len(cons) == 4:
            if trips == "":
                trips = cons[0]
                ## print("trip: " + str(cons[0]) + " found at index: " + str(index))
            return trips, fives
        if len(cons) >= 5:
            if fives == "":
                fives += str(cons[0])
                ## print("fives: " + str(cons[0]) + " found at index: " + str(index))
    return trips, fives    

## part 2 bugging... right answer still at position 63, not 64